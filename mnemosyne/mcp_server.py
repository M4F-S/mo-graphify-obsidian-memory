"""MCP server (JSON-RPC 2.0 over stdio)."""

import sys
import json
import logging
from typing import Dict, List, Optional

from mnemosyne.core import UnifiedMemorySystem

logger = logging.getLogger("unified-memory")


class MemoryMCPServer:
    """
    MCP server exposing memory operations as tools.
    Compatible with Claude Code, Cursor, and any MCP client.
    """

    def __init__(self, memory: Optional[UnifiedMemorySystem] = None):
        self._memory = memory

    @property
    def memory(self) -> UnifiedMemorySystem:
        if self._memory is None:
            self._memory = UnifiedMemorySystem(auto_sync=False)
        return self._memory

    def run(self):
        """Main loop: read JSON-RPC requests from stdin, write responses to stdout."""
        logger.info("MCP Memory Server starting...")
        for line in sys.stdin:
            line = line.strip()
            if not line:
                continue
            req_id = None
            try:
                req = json.loads(line)
                req_id = req.get("id")
                resp = self._handle(req)
            except json.JSONDecodeError as e:
                resp = {"jsonrpc": "2.0", "error": {"code": -32700, "message": str(e)}, "id": req_id}
            except Exception as e:
                resp = {"jsonrpc": "2.0", "error": {"code": -32603, "message": str(e)}, "id": req_id}
            print(json.dumps(resp), flush=True)

    def _handle(self, req: Dict) -> Dict:
        """Handle a single JSON-RPC request."""
        method = req.get("method")
        params = req.get("params", {})
        req_id = req.get("id")

        if method == "initialize":
            return {"jsonrpc": "2.0", "result": {"protocolVersion": "2024-11-05", "capabilities": {}}, "id": req_id}
        if method == "tools/list":
            return {"jsonrpc": "2.0", "result": {"tools": self._tools()}, "id": req_id}
        if method == "tools/call":
            name = params.get("name", "")
            args = params.get("arguments", {})
            result = self._call_tool(name, args)
            return {"jsonrpc": "2.0", "result": {"content": [{"type": "text", "text": json.dumps(result)}]}, "id": req_id}
        return {"jsonrpc": "2.0", "error": {"code": -32601, "message": f"Method not found: {method}"}, "id": req_id}

    def _tools(self) -> List[Dict]:
        return [
            {
                "name": "memory_remember",
                "description": "Save a fact, decision, or observation to persistent memory",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "title": {"type": "string"},
                        "content": {"type": "string"},
                        "tags": {"type": "array", "items": {"type": "string"}},
                        "salience": {"type": "number"}
                    },
                    "required": ["title", "content"]
                }
            },
            {
                "name": "memory_recall",
                "description": "Search memory by semantic meaning, keywords, or graph relationships",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "query": {"type": "string"},
                        "mode": {"type": "string", "enum": ["hybrid", "semantic", "keyword", "graph"]},
                        "top_k": {"type": "integer", "default": 5}
                    },
                    "required": ["query"]
                }
            },
            {
                "name": "memory_remind_me",
                "description": "Schedule a future reminder or recurring task",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "title": {"type": "string"},
                        "content": {"type": "string"},
                        "trigger_at": {"type": "string"},
                        "recurring": {"type": "string", "enum": ["daily", "weekly", "monthly"]}
                    },
                    "required": ["title", "trigger_at"]
                }
            },
            {
                "name": "memory_audit",
                "description": "Get memory system statistics and health check",
                "inputSchema": {"type": "object", "properties": {}}
            }
        ]

    def _call_tool(self, name: str, args: Dict) -> Dict:
        if name == "memory_remember":
            return self.memory.remember(title=args.get("title", ""), content=args.get("content", ""), tags=args.get("tags", []), salience=args.get("salience"))
        elif name == "memory_recall":
            return {"results": self.memory.recall(query=args.get("query", ""), mode=args.get("mode", "hybrid"), top_k=args.get("top_k", 5))}
        elif name == "memory_remind_me":
            return {"reminder_id": self.memory.remind_me(title=args.get("title", ""), trigger_at=args.get("trigger_at", ""), content=args.get("content", ""), recurring=args.get("recurring"))}
        elif name == "memory_audit":
            return self.memory.stats()
        else:
            return {"error": f"Unknown tool: {name}"}
