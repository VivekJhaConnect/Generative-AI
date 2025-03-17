"""
1. Run: `pip install openai lancedb tantivy pypdf sqlalchemy phidata` to install the dependencies
2. Run: `python cookbook/rag/04_agentic_rag_lancedb.py` to run the agent
"""

from phi.agent import Agent
from phi.knowledge.pdf import PDFUrlKnowledgeBase
from phi.vectordb.chroma import ChromaDb
from llm_environment import client

# Initialize ChromaDB
vector_db = ChromaDb(collection="recipes", path="tmp/chromadb", persistent_client=True)

# Create knowledge base
knowledge_base = PDFUrlKnowledgeBase(
    urls=["https://phi-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
    vector_db=vector_db,
)
# Load the knowledge base: Comment after first run as the knowledge base is already loaded
knowledge_base.load()

# Create and use the agent
agent = Agent(knowledge_base=knowledge_base, use_tools=True, show_tool_calls=True)
agent.print_response("Show me how to make Tom Kha Gai", markdown=True)
