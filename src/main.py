"""
Inductive Bible Study Agent - Main Entry Point

This module serves as the entry point for the Inductive Bible Study Agent.
It initializes the agent and manages the main application flow.

Author: Inductive Study Agent Team
Version: 0.1.0
"""

import sys
import os
from pathlib import Path

# Add src directory to path
sys.path.insert(0, str(Path(__file__).parent))


def main():
    """
    Main application entry point.
    
    Initializes the Inductive Bible Study Agent and starts the interaction loop.
    """
    try:
        # Import agent components
        from agent.bible_study_agent import BibleStudyAgent
        from utils.logging import setup_logging
        
        # Setup logging
        logger = setup_logging()
        logger.info("Starting Inductive Bible Study Agent")
        
        # Initialize the agent
        agent = BibleStudyAgent()
        
        # Start the agent conversation loop
        print("\n" + "="*60)
        print("  Inductive Bible Study Agent v0.1.0")
        print("="*60)
        print("\nWelcome! I'm here to guide you through inductive Bible study.")
        print("\nYou can ask me things like:")
        print('  - "Do an inductive study on John 3:16"')
        print('  - "Tell me more about Romans 8:28"')
        print('  - "What does Psalm 23:1 mean?"')
        print('\nType "exit" to quit.\n')
        
        # Main conversation loop
        while True:
            try:
                user_input = input("You: ").strip()
                
                if not user_input:
                    continue
                
                if user_input.lower() in ['exit', 'quit', 'bye']:
                    print("\nAgent: Thank you for studying Scripture with me. May the Word of God transform your life!")
                    break
                
                # Get agent response
                response = agent.process_query(user_input)
                print(f"\nAgent: {response}\n")
                
            except KeyboardInterrupt:
                print("\n\nAgent: Goodbye! Keep studying God's Word.")
                break
            except Exception as e:
                logger.error(f"Error processing query: {str(e)}")
                print(f"Agent: I encountered an error: {str(e)}")
                print("Please try again with a different question.\n")
        
    except ImportError as e:
        print(f"Error: Could not import required modules: {e}")
        print("Please ensure all dependencies are installed:")
        print("  pip install -r requirements.txt")
        sys.exit(1)
    except Exception as e:
        print(f"Fatal error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
