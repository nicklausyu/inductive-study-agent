# Agent Skills Documentation

## Overview

The Inductive Bible Study Agent operates through a collection of specialized skills that work together to provide comprehensive biblical analysis. Each skill focuses on a specific aspect of the inductive study method and can be used independently or in combination.

## Skills Summary

| Skill | Phase | Purpose | Key Outputs |
|-------|-------|---------|-------------|
| **Observation** | 1 | Text analysis | Key words, structure, patterns |
| **Interpretation** | 2 | Meaning analysis | Theology, grammar, significance |
| **Cultural Context** | 2 | Historical insight | Background, customs, society |
| **Linguistic** | 2 | Language analysis | Greek/Hebrew, etymology |
| **Cross-Reference** | 3 | Connection finding | Related passages, themes |
| **Application** | 3 | Personal guidance | Principles, steps, questions |

---

## Skill Details

### 1. Observation Skill

**Purpose**: Perform detailed analysis of what the text actually says

**Key Functions**:
- Identify key words and repeated phrases
- Analyze sentence structure and grammar
- Note literary devices (metaphor, parallelism, etc.)
- Identify genre indicators
- Highlight questions or tensions in the text
- Map the flow of thought

**Example Output**:
```
Key Terms:
- "Beloved" (agapetos - dear, beloved)
- "World" (kosmos - ordered system)
- "Perish" (apollymi - to destroy, be ruined)

Structure:
- Conditional statement ("For God so loved...")
- Purpose clause ("...that whoever believes...")
- Result statement ("...should not perish...")

Repetitions:
- Reference to God's love (foundation)
- "Whoever" (inclusive emphasis)
```

**Configuration**:
```json
{
  "include_grammar": true,
  "identify_repetitions": true,
  "note_literary_devices": true,
  "highlight_questions": true
}
```

---

### 2. Interpretation Skill

**Purpose**: Explain the meaning and theological significance of the passage

**Key Functions**:
- Analyze grammatical relationships
- Explain theological concepts
- Connect to doctrinal themes
- Interpret symbolism and imagery
- Provide contextual meaning
- Address interpretive debates

**Example Output**:
```
Theological Significance:
- God's sacrificial love for humanity
- Universal scope of salvation
- Centrality of belief in salvation

Doctrinal Connections:
- God's love (1 John 4:7-8)
- Redemption through Christ
- The nature of faith

Key Concepts:
- Agape love (self-giving, unconditional)
- Cosmos (the world system in rebellion)
- Eternal life (zoe - quality of life with God)
```

**Configuration**:
```json
{
  "include_theology": true,
  "acknowledge_debates": true,
  "depth": "comprehensive"
}
```

---

### 3. Cultural Context Skill

**Purpose**: Illuminate the historical and cultural world of the passage

**Key Functions**:
- Provide historical background
- Explain cultural practices and customs
- Contextualize geographical references
- Describe societal norms and expectations
- Explain religious context
- Clarify political situations

**Example Output**:
```
Historical Context:
- Written during Roman occupation of Palestine
- First-century Jewish religious landscape
- Greco-Roman philosophical environment

Cultural Practices:
- Jewish understanding of "world"
- First-century salvation expectations
- Relationship between faith and works in Judaism

Social Context:
- Jewish-Gentile relations
- Religious authority structures
- Common misconceptions about salvation
```

**Configuration**:
```json
{
  "era_focus": "first_century",
  "include_political": true,
  "include_social": true,
  "include_religious": true
}
```

---

### 4. Linguistic Analysis Skill

**Purpose**: Explore the original language nuances and meanings

**Key Functions**:
- Analyze Greek (NT) and Hebrew (OT) words
- Explain etymologies and word families
- Note translation variations across versions
- Highlight nuances lost in translation
- Compare word usage across Scripture
- Explain grammatical significance

**Example Output**:
```
Greek Analysis:
- "agapao" (αγαπαω) - to love sacrificially
  * Root: agape (selfless, unconditional love)
  * Usage: 140 times in NT
  * Contrast: "phileo" (brotherly love)

Word Studies:
- "kosmos" (κοσμος) - ordered system/world
  * Can mean: physical world, humanity, world system
  * Here: humanity in rebellion against God

Translation Notes:
- KJV "begotten" vs. NASB "only" - emphasis difference
- Modern versions use "one and only" or "one of a kind"
```

**Configuration**:
```json
{
  "include_transliteration": true,
  "explain_etymology": true,
  "compare_translations": true,
  "note_nuances": true
}
```

---

### 5. Cross-Reference Skill

**Purpose**: Identify and connect related biblical passages

**Key Functions**:
- Find passages with similar themes
- Identify parallel accounts (especially in Gospels)
- Locate fulfilled prophecies
- Show doctrinal development across Scripture
- Connect Old Testament and New Testament
- Find applications of principles elsewhere

**Example Output**:
```
Thematic Connections:
- 1 John 4:7-8 (Nature of God's love)
- Romans 5:8 (Christ's sacrificial love)
- Ephesians 2:4-5 (God's mercy and love)

Parallel Passages:
- Matthew 18:11 (Jesus came to seek the lost)
- Luke 15:1-7 (Parable of the lost sheep)

Old Testament Echoes:
- Exodus 34:6-7 (God's mercy and grace)
- Isaiah 53 (Suffering servant prophecy)
- Hosea 11:1 (God's love for Israel)

Doctrinal Development:
- Progressive revelation of God's love plan
- Foundation in Old Testament covenant
- Fulfillment in Christ
- Application in church age
```

**Configuration**:
```json
{
  "max_references": 10,
  "include_old_testament": true,
  "include_new_testament": true,
  "relevance_threshold": 0.7
}
```

---

### 6. Application Skill

**Purpose**: Guide personal and practical application of biblical truth

**Key Functions**:
- Identify timeless biblical principles
- Connect ancient truth to modern contexts
- Suggest practical life applications
- Provide reflection questions
- Encourage personal study and prayer
- Suggest accountability and discussion opportunities

**Example Output**:
```
Timeless Principles:
1. God's love for us is unconditional and sacrificial
2. Salvation requires personal faith and commitment
3. God desires relationship with all humanity
4. Love should motivate our lives and decisions

Personal Application:
- Have I truly grasped God's love for me personally?
- Does my faith rest in Christ's work or something else?
- Am I extending God's love to others?

Practical Steps:
1. Meditate on God's love this week
2. Share your faith story with someone
3. Pray for someone far from God
4. Join a Bible study on this passage

Reflection Questions:
- What aspect of God's love impacts me most?
- How has this truth changed my perspective?
- Who needs to hear about God's love through me?
- What step of faith is God calling me to take?
```

**Configuration**:
```json
{
  "include_questions": true,
  "practical_focus": true,
  "include_challenges": true,
  "suggest_actions": true
}
```

---

## Skill Activation and Orchestration

### Default Behavior
All six skills are enabled by default and activated based on the user's intent:

- **Full Study Request**: All six skills activated
- **Quick Lookup**: Observation, Interpretation, Application
- **Context Question**: Cultural Context, Linguistic
- **Application Focus**: Application, Cross-Reference

### Intent Recognition

The agent recognizes user intent through pattern matching:

```javascript
Full Study: "Do an inductive study on...", "Study...", "Analyze..."
Quick Lookup: "What does...mean?", "Explain...", "Tell me about..."
Context Focus: "Background of...", "Why was...written?", "Context of..."
Application: "How do I apply...?", "Relevant today?", "How to live out..."
```

### Skill Composition

Skills work together in predefined combinations:

1. **Observation Phase**: Observation skill
2. **Interpretation Phase**: Interpretation, Cultural Context, Linguistic
3. **Application Phase**: Application, Cross-Reference

### Customization

Users can request specific skills:
- "Just give me the cultural background"
- "Focus on the Greek language here"
- "What are some applications?"

---

## Skill Parameters and Configuration

Each skill has configurable parameters in `config/skills_config.json`:

```json
{
  "id": "skill_name",
  "name": "Skill Display Name",
  "enabled": true,
  "priority": 1,
  "capabilities": ["capability1", "capability2"],
  "parameters": {
    "param1": "value1",
    "param2": "value2"
  }
}
```

### Adjusting Skill Parameters

To customize skill behavior:

1. Edit `config/skills_config.json`
2. Modify parameter values
3. Restart the agent
4. Changes apply immediately

---

## Performance Characteristics

| Skill | Speed | Accuracy | Resource Use |
|-------|-------|----------|--------------|
| Observation | Fast | Very High | Low |
| Interpretation | Medium | High | Medium |
| Cultural Context | Medium | High | Medium |
| Linguistic | Fast | Very High | Low |
| Cross-Reference | Fast | High | Low |
| Application | Medium | High | Medium |

---

## Best Practices

### For Users
1. **Start with Observation**: Understand the text first
2. **Use Context**: Cultural knowledge enriches meaning
3. **Apply Personally**: Move from head to heart
4. **Use Cross-References**: See biblical connections
5. **Ask Questions**: Engage with the text critically

### For Developers
1. **Keep Skills Focused**: One responsibility per skill
2. **Test Thoroughly**: Validate all outputs
3. **Document Sources**: Cite biblical scholarship
4. **Handle Edge Cases**: Unknown verses, unclear references
5. **Monitor Performance**: Track skill execution time

---

## Extending Skills

### Creating a New Skill

1. **Create Skill File**:
```python
# src/skills/new_skill.py
from skills.base_skill import BaseSkill

class NewSkill(BaseSkill):
    def analyze(self, passage):
        # Implement analysis logic
        pass
```

2. **Register in Configuration**:
```json
{
  "id": "new_skill",
  "name": "New Skill Name",
  "enabled": true,
  "priority": 7,
  "capabilities": ["capability1"],
  "parameters": {}
}
```

3. **Update Agent Logic**:
Modify `src/agent/skill_orchestrator.py` to activate the skill

4. **Test Thoroughly**:
Add tests in `tests/test_skills.py`

---

## Troubleshooting

### Skill Not Activated
- Check `enabled` flag in configuration
- Verify intent recognition is matching
- Check skill priority ordering

### Inaccurate Results
- Verify input passage is correctly parsed
- Check skill parameters
- Review biblical data sources
- Compare with multiple translations

### Performance Issues
- Check skill parameters for scope
- Limit cross-references count
- Disable non-essential skills
- Review API usage patterns

---

For implementation details and code examples, see the individual skill files in `src/skills/`.
