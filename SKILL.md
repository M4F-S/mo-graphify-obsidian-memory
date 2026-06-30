---
name: mo-graphify-obsidian-memory
description: >
  Build and manage a graph-based knowledge memory system using Obsidian markdown vault files.
  Creates interconnected notes with YAML frontmatter, wiki-links [[Note Name]], and graph
  visualizations. Enables knowledge persistence, concept relationships, and memory retrieval
  as a structured graph. Triggered by: "graphify my knowledge", "obsidian memory system",
  "knowledge graph", "memory vault", "graph notes", "obsidian notes", "note linking",
  "concept map", "second brain", "Zettelkasten", "build knowledge graph from notes".
---

# mo-Graphify + Obsidian Memory

Build and manage a graph-based knowledge memory system using Obsidian markdown vault files.

## Overview

This skill enables any Kimi session to create, read, update, and link markdown notes in an Obsidian-compatible vault. Notes are stored as plain markdown files with YAML frontmatter, connected via wiki-links `[[Note Name]]`, and can be visualized as a knowledge graph.

| Concept | Description |
|---------|-------------|
| **Vault** | Directory containing all markdown notes |
| **Note** | Single markdown file with YAML frontmatter + body |
| **Wiki-Link** | `[[Note Title]]` syntax for bidirectional linking |
| **Frontmatter** | YAML metadata at the top of each note (tags, dates, type) |
| **Graph** | Visual network of notes and their relationships |
| **MOC** | Map of Content — a hub note that links to related topics |

## Default Vault Location

```bash
VAULT_PATH="/Users/mohamedfathy/Documents/Kimi/Workspaces/Mnemosyne/obsidian-vault"
```

Create the vault if it doesn't exist:
```bash
mkdir -p "$VAULT_PATH"
```

---

## Note Format

Every note follows the Obsidian standard format:

```markdown
---
title: Note Title
date: 2026-06-30
tags: [concept, tag1, tag2]
type: concept  # concept | task | person | project | reference | MOC
status: active  # active | archived | draft
links: [[Related Note 1]], [[Related Note 2]]
---

# Note Title

Content goes here. Use wiki-links to connect ideas:
- This relates to [[Another Concept]]
- See also [[Project Alpha]] for implementation details

## Key Points

- Point 1
- Point 2

## References

- [Source URL](https://example.com)
```

---

## Core Operations

### 1. Create a Note

```python
import os
from datetime import datetime

VAULT_PATH = "/Users/mohamedfathy/Documents/Kimi/Workspaces/Mnemosyne/obsidian-vault"

def create_note(title, content, tags=None, note_type="concept", links=None):
    """Create a new markdown note with YAML frontmatter."""
    tags = tags or []
    links = links or []
    
    safe_filename = title.replace(" ", "-").replace("/", "-") + ".md"
    filepath = os.path.join(VAULT_PATH, safe_filename)
    
    frontmatter = f"""---
title: {title}
date: {datetime.now().strftime('%Y-%m-%d')}
tags: {tags}
type: {note_type}
status: active
links: {', '.join(f'[[{l}]]' for l in links)}
---

# {title}

{content}
"""
    
    with open(filepath, 'w') as f:
        f.write(frontmatter)
    
    return filepath

# Example usage:
# create_note(
#     title="Machine Learning Basics",
#     content="Machine learning is a subset of AI...",
#     tags=["ai", "ml", "foundation"],
#     note_type="concept",
#     links=["Deep Learning", "Neural Networks"]
# )
```

### 2. Read a Note

```python
def read_note(title):
    """Read a note by title."""
    safe_filename = title.replace(" ", "-").replace("/", "-") + ".md"
    filepath = os.path.join(VAULT_PATH, safe_filename)
    
    if not os.path.exists(filepath):
        return None
    
    with open(filepath, 'r') as f:
        return f.read()

# Example:
# content = read_note("Machine Learning Basics")
```

### 3. Update a Note

```python
def update_note(title, new_content=None, append_content=None, new_tags=None, new_links=None):
    """Update an existing note."""
    safe_filename = title.replace(" ", "-").replace("/", "-") + ".md"
    filepath = os.path.join(VAULT_PATH, safe_filename)
    
    if not os.path.exists(filepath):
        return None
    
    with open(filepath, 'r') as f:
        existing = f.read()
    
    # Parse frontmatter and body
    if existing.startswith('---'):
        parts = existing.split('---', 2)
        frontmatter = parts[1]
        body = parts[2] if len(parts) > 2 else ""
    else:
        frontmatter = ""
        body = existing
    
    # Update content
    if new_content:
        body = f"\n# {title}\n\n" + new_content
    elif append_content:
        body += "\n\n" + append_content
    
    # Reconstruct with updated frontmatter if needed
    # (simplified - in production, parse YAML properly)
    updated = f"---{frontmatter}---{body}"
    
    with open(filepath, 'w') as f:
        f.write(updated)
    
    return filepath
```

### 4. Search Notes

```python
import glob

def search_notes(query, search_tags=None):
    """Search notes by content or tags."""
    results = []
    
    for filepath in glob.glob(os.path.join(VAULT_PATH, "*.md")):
        with open(filepath, 'r') as f:
            content = f.read()
        
        if query.lower() in content.lower():
            results.append(os.path.basename(filepath)[:-3])
    
    return results

# Example:
# search_notes("neural network")
```

### 5. List All Notes

```bash
# List all notes in the vault
ls -la "$VAULT_PATH"/*.md 2>/dev/null

# Count notes
echo "Total notes: $(ls "$VAULT_PATH"/*.md 2>/dev/null | wc -l)"
```

---

## Knowledge Graph Visualization

### Generate Graph Data (JSON for D3.js or similar)

```python
import json
import re

def generate_graph_data():
    """Generate nodes and edges from the vault for graph visualization."""
    nodes = []
    edges = []
    node_map = {}
    
    for filepath in glob.glob(os.path.join(VAULT_PATH, "*.md")):
        filename = os.path.basename(filepath)[:-3]
        title = filename.replace("-", " ")
        
        with open(filepath, 'r') as f:
            content = f.read()
        
        # Extract tags from frontmatter
        tags = []
        tag_match = re.search(r'tags:\s*\[(.*?)\]', content)
        if tag_match:
            tags = [t.strip().strip('"\'') for t in tag_match.group(1).split(',')]
        
        # Extract type
        note_type = "concept"
        type_match = re.search(r'type:\s*(\w+)', content)
        if type_match:
            note_type = type_match.group(1)
        
        # Add node
        node_id = len(nodes)
        node_map[title] = node_id
        nodes.append({
            "id": node_id,
            "label": title,
            "type": note_type,
            "tags": tags,
            "file": filename
        })
        
        # Extract wiki-links
        wiki_links = re.findall(r'\[\[(.*?)\]\]', content)
        for link in wiki_links:
            edges.append({
                "source": title,
                "target": link.strip()
            })
    
    # Resolve edge IDs
    resolved_edges = []
    for edge in edges:
        if edge["source"] in node_map and edge["target"] in node_map:
            resolved_edges.append({
                "source": node_map[edge["source"]],
                "target": node_map[edge["target"]]
            })
    
    return {"nodes": nodes, "edges": resolved_edges}

# Save graph data
# graph = generate_graph_data()
# with open(os.path.join(VAULT_PATH, "graph-data.json"), 'w') as f:
#     json.dump(graph, f, indent=2)
```

### Generate Mermaid Graph

```python
def generate_mermaid_graph(max_nodes=50):
    """Generate a Mermaid diagram of the knowledge graph."""
    graph = generate_graph_data()
    
    mermaid = ["graph LR"]
    
    # Add nodes (limited to prevent diagram bloat)
    for node in graph["nodes"][:max_nodes]:
        mermaid.append(f'    {node["id"]}["{node["label"]}"]')
    
    # Add edges
    for edge in graph["edges"]:
        if edge["source"] < max_nodes and edge["target"] < max_nodes:
            mermaid.append(f'    {edge["source"]} --> {edge["target"]}')
    
    return "\n".join(mermaid)

# Example output:
# graph LR
#     0["Machine Learning Basics"]
#     1["Deep Learning"]
#     2["Neural Networks"]
#     0 --> 1
#     0 --> 2
```

---

## Map of Content (MOC) Notes

MOCs are hub notes that organize related concepts. Create them as central navigation points.

### Create a MOC

```python
def create_moc(title, description, related_notes):
    """Create a Map of Content note."""
    content = f"""{description}

## Overview

This MOC connects the following concepts:

"""
    for note in related_notes:
        content += f"- [[{note}]]\n"
    
    content += """
## Connections

"""
    
    return create_note(
        title=title,
        content=content,
        tags=["MOC", "index"],
        note_type="MOC",
        links=related_notes
    )

# Example:
# create_moc(
#     title="AI Knowledge Map",
#     description="Central hub for all artificial intelligence concepts.",
#     related_notes=["Machine Learning Basics", "Deep Learning", "Neural Networks", "Transformers"]
# )
```

---

## Memory Management Patterns

### Pattern 1: Daily Notes

Create a daily note to capture transient thoughts and link them to permanent notes:

```python
def create_daily_note():
    """Create a daily note for capturing thoughts."""
    today = datetime.now().strftime('%Y-%m-%d')
    title = f"Daily Note {today}"
    
    content = f"""## Morning Thoughts

- 

## Key Learnings

- 

## Links Created

- [[ ]]

## Tasks

- [ ] 
"""
    
    return create_note(
        title=title,
        content=content,
        tags=["daily", "journal"],
        note_type="journal"
    )
```

### Pattern 2: Concept Notes (Permanent Notes)

Atomic, self-contained notes about single concepts:

```python
def create_concept_note(concept, definition, related_concepts=None, sources=None):
    """Create an atomic concept note."""
    related = related_concepts or []
    refs = sources or []
    
    content = f"""{definition}

## Key Properties

- 

## Related Concepts

"""
    for rc in related:
        content += f"- [[{rc}]]\n"
    
    if refs:
        content += """
## Sources

"""
        for ref in refs:
            content += f"- {ref}\n"
    
    return create_note(
        title=concept,
        content=content,
        tags=["concept"],
        note_type="concept",
        links=related
    )
```

### Pattern 3: Project Notes

Track projects with status, tasks, and linked concepts:

```python
def create_project_note(project_name, description, tasks=None, linked_concepts=None):
    """Create a project tracking note."""
    task_list = tasks or []
    concepts = linked_concepts or []
    
    content = f"""{description}

## Status

Active

## Tasks

"""
    for task in task_list:
        content += f"- [ ] {task}\n"
    
    content += """
## Related Concepts

"""
    for concept in concepts:
        content += f"- [[{concept}]]\n"
    
    return create_note(
        title=project_name,
        content=content,
        tags=["project"],
        note_type="project",
        links=concepts
    )
```

---

## Integration with Other Tools

### Sync with Kimi Memory

```python
def sync_to_kimi_memory(note_title, memory_path="/Users/mohamedfathy/Documents/Kimi/Workspaces/Mnemosyne/memory"):
    """Copy a note's content to Kimi's memory directory."""
    content = read_note(note_title)
    if not content:
        return None
    
    memory_file = os.path.join(memory_path, f"{note_title.replace(' ', '_')}.md")
    os.makedirs(memory_path, exist_ok=True)
    
    with open(memory_file, 'w') as f:
        f.write(content)
    
    return memory_file
```

### Export as JSON

```python
def export_vault_to_json(output_path=None):
    """Export the entire vault as structured JSON."""
    if output_path is None:
        output_path = os.path.join(VAULT_PATH, "vault-export.json")
    
    vault = {
        "vault_path": VAULT_PATH,
        "notes": [],
        "graph": generate_graph_data()
    }
    
    for filepath in glob.glob(os.path.join(VAULT_PATH, "*.md")):
        with open(filepath, 'r') as f:
            content = f.read()
        
        vault["notes"].append({
            "filename": os.path.basename(filepath),
            "content": content
        })
    
    with open(output_path, 'w') as f:
        json.dump(vault, f, indent=2)
    
    return output_path
```

---

## Best Practices

1. **Atomic Notes** — Each note should cover one concept. If it gets too long, split it.
2. **Link Aggressively** — Every new note should link to at least 2 existing notes.
3. **Use Tags Sparingly** — Tags are for broad categories; links are for specific relationships.
4. **Create MOCs** — When you have 7+ notes on a topic, create a Map of Content.
5. **Review Weekly** — Run `search_notes` to find orphaned notes (notes with no links).
6. **Back Up** — The vault is just markdown files. Sync to GitHub or cloud storage.
7. **Naming** — Use descriptive titles. The note filename becomes the node label in the graph.
8. **Frontmatter** — Always include `type` and `tags` for filtering and organization.

---

## Quick Reference

| Operation | Command / Function |
|-----------|-------------------|
| Create note | `create_note(title, content, tags, type, links)` |
| Read note | `read_note(title)` |
| Update note | `update_note(title, new_content)` |
| Search | `search_notes(query)` |
| List all | `glob.glob(os.path.join(VAULT_PATH, "*.md"))` |
| Graph data | `generate_graph_data()` |
| Mermaid graph | `generate_mermaid_graph()` |
| Create MOC | `create_moc(title, desc, related_notes)` |
| Daily note | `create_daily_note()` |
| Concept note | `create_concept_note(concept, definition, related)` |
| Project note | `create_project_note(name, desc, tasks, concepts)` |
| Export JSON | `export_vault_to_json()` |

---

## Example Workflow

```python
# 1. Initialize vault
VAULT_PATH = "/Users/mohamedfathy/Documents/Kimi/Workspaces/Mnemosyne/obsidian-vault"

# 2. Create foundational concepts
create_concept_note(
    concept="Neural Networks",
    definition="Neural networks are computing systems inspired by biological neural networks...",
    related_concepts=["Deep Learning", "Backpropagation"],
    sources=["[Goodfellow et al., Deep Learning](http://www.deeplearningbook.org/)"]
)

create_concept_note(
    concept="Deep Learning",
    definition="Deep learning is a subset of machine learning based on artificial neural networks...",
    related_concepts=["Neural Networks", "Machine Learning Basics"]
)

# 3. Create a MOC
create_moc(
    title="AI Knowledge Map",
    description="Central hub for AI concepts.",
    related_notes=["Neural Networks", "Deep Learning"]
)

# 4. Generate graph
graph = generate_mermaid_graph()
print(graph)
```
