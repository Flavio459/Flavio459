#!/usr/bin/env python3
"""
GitHub Repository Labels Automation Script

This script automatically creates and assigns labels to your GitHub repositories
based on the repository mapping configuration.

Usage:
    python scripts/setup_labels.py

Requirements:
    pip install PyGithub python-dotenv

Setup:
    1. Create a GitHub Personal Access Token (PAT) with 'repo' scope
    2. Set environment variable: export GITHUB_TOKEN='your_token_here'
    3. Run the script
"""

import os
import sys
from typing import Dict, List
from github import Github, GithubException
from datetime import datetime

# Label definitions
LABEL_CONFIG = {
    # Status Labels
    'active': {
        'color': '28a745',
        'description': 'Actively developed'
    },
    'paused': {
        'color': 'ffa500',
        'description': 'Development on hold'
    },
    'maintenance-only': {
        'color': 'cccccc',
        'description': 'Bug fixes only'
    },
    'archived': {
        'color': '6f42c1',
        'description': 'Legacy projects'
    },
    'deprecated': {
        'color': 'dd3333',
        'description': 'No longer used'
    },
    
    # Feature Labels
    'ai-powered': {
        'color': '0366d6',
        'description': 'Uses AI/LLM'
    },
    'app-core': {
        'color': '1f6feb',
        'description': 'Main business application'
    },
    'integration': {
        'color': '6f42c1',
        'description': 'Third-party integrations'
    },
    'experimental': {
        'color': 'fbca04',
        'description': 'POCs & tests'
    },
    'documentation': {
        'color': '0075ca',
        'description': 'Docs & specifications'
    },
    
    # Type Labels
    'typescript': {
        'color': '2b7489',
        'description': 'TypeScript/JavaScript'
    },
    'python': {
        'color': '3572A5',
        'description': 'Python'
    },
    'fullstack': {
        'color': '11854e',
        'description': 'Frontend + Backend'
    },
    'frontend': {
        'color': 'e8f026',
        'description': 'UI focused'
    },
    'open-source': {
        'color': '34495e',
        'description': 'Public contributions'
    },
    
    # Audience Labels
    'commercial': {
        'color': 'd4af37',
        'description': 'Business/Wii Group'
    },
    'personal-project': {
        'color': 'f9c74f',
        'description': 'Personal use'
    },
}

# Repository to Labels mapping
REPO_LABELS_MAP = {
    'Alma-Ego': ['ai-powered', 'app-core', 'typescript', 'active', 'commercial'],
    'synapsehub-workspace': ['app-core', 'typescript', 'fullstack', 'active', 'commercial'],
    'PH-ICE-PMOC-Assistente': ['app-core', 'typescript', 'commercial', 'active'],
    'IAStudio': ['experimental', 'typescript', 'app-core', 'active'],
    'Assistente-de-Compras-IA': ['ai-powered', 'typescript', 'app-core', 'active', 'commercial'],
    'indai--delivery-assit': ['app-core', 'commercial', 'integration', 'active'],
    'https-github.com-Flavio459-phice': ['app-core', 'typescript', 'frontend', 'active', 'commercial'],
    
    'Trello-AdvocacIA': ['paused', 'integration', 'javascript'],
    'lyra-ai-nexus': ['paused', 'experimental', 'typescript'],
    'project-bolt-sb1-juz4lmxb': ['paused', 'experimental', 'typescript'],
    'Pub-Board-Game-Experience': ['paused', 'frontend', 'html'],
    
    'git-EFBarros': ['integration', 'typescript', 'personal-project', 'active'],
    'Medium-Integration-API---OpenAPI-Specification': ['documentation', 'integration', 'open-source'],
    'N8N': ['integration', 'active', 'commercial'],
    
    'OpenManus': ['fork', 'open-source', 'python', 'active'],
    'tldraw': ['fork', 'open-source', 'typescript', 'active'],
    'Quebra-de-Obje-es-PHICE': ['open-source', 'javascript', 'experimental'],
    'Flavio459': ['documentation', 'active'],
    
    'desktop-tutorial': ['personal-project', 'archived'],
    'BlogGeniusV2': ['archived', 'python', 'deprecated'],
    'Mentor-GPT-SUP.py': ['archived', 'python', 'deprecated'],
    'Instenergy': ['archived', 'maintenance-only'],
    'Python-1': ['archived', 'maintenance-only', 'python'],
    'copy-of-ph-ice---climatiza--o-inteligente': ['app-core', 'typescript', 'commercial', 'active'],
    'Economia-Familiar': ['personal-project', 'archived'],
}

def setup_labels(repo) -> Dict[str, int]:
    """Create all labels in repository."""
    created = 0
    existing = 0
    
    print(f"  Setting up labels in {repo.name}...")
    
    for label_name, label_config in LABEL_CONFIG.items():
        try:
            repo.create_label(
                name=label_name,
                color=label_config['color'],
                description=label_config['description']
            )
            created += 1
            print(f"    ✓ Created label: {label_name}")
        except GithubException as e:
            if e.status == 422:  # Label already exists
                existing += 1
            else:
                print(f"    ✗ Error creating {label_name}: {e}")
    
    return {'created': created, 'existing': existing}

def assign_labels(repo, labels: List[str]) -> int:
    """Assign labels to repository topics/metadata."""
    added = 0
    
    print(f"  Assigning {len(labels)} labels to repository...")
    
    try:
        # Add labels to repository (as topics)
        repo.edit(topics=labels)
        added = len(labels)
        print(f"    ✓ Added {len(labels)} labels as topics")
    except GithubException as e:
        print(f"    ✗ Error assigning labels: {e}")
    
    return added

def main():
    """Main execution function."""
    print("\n" + "="*60)
    print("GitHub Repository Labels Automation")
    print("="*60 + "\n")
    
    # Get GitHub token
    token = os.getenv('GITHUB_TOKEN')
    if not token:
        print("❌ Error: GITHUB_TOKEN environment variable not set!")
        print("\nSetup instructions:")
        print("1. Create a GitHub Personal Access Token (PAT)")
        print("2. Set environment variable: export GITHUB_TOKEN='your_token_here'")
        print("3. Run this script again\n")
        sys.exit(1)
    
    try:
        # Initialize GitHub client
        g = Github(token)
        user = g.get_user()
        print(f"✓ Connected as: {user.login}\n")
        
        stats = {
            'repos_processed': 0,
            'labels_created': 0,
            'labels_assigned': 0,
            'errors': 0
        }
        
        # Process each repository
        for repo_name, labels in REPO_LABELS_MAP.items():
            try:
                print(f"\nProcessing: {repo_name}")
                repo = user.get_repo(repo_name)
                
                # Setup labels in repository
                label_stats = setup_labels(repo)
                stats['labels_created'] += label_stats['created']
                
                # Assign specific labels to this repo
                assigned = assign_labels(repo, labels)
                stats['labels_assigned'] += assigned
                stats['repos_processed'] += 1
                
            except GithubException as e:
                print(f"✗ Error processing {repo_name}: {e}")
                stats['errors'] += 1
        
        # Summary
        print("\n" + "="*60)
        print("SUMMARY")
        print("="*60)
        print(f"Repositories processed: {stats['repos_processed']}")
        print(f"Labels created: {stats['labels_created']}")
        print(f"Labels assigned: {stats['labels_assigned']}")
        print(f"Errors: {stats['errors']}")
        print("="*60 + "\n")
        
        if stats['errors'] == 0:
            print("✅ All repositories labeled successfully!\n")
        else:
            print(f"⚠️  {stats['errors']} errors encountered. Please review.\n")
            sys.exit(1)
    
    except Exception as e:
        print(f"\n❌ Fatal error: {e}\n")
        sys.exit(1)

if __name__ == '__main__':
    main()
