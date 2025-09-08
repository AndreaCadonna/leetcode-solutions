# 📝 Markdown Style Guide for Algorithm Explanation Documents

## 🎯 Design Philosophy

Create **comprehensive, well-structured, and visually appealing** algorithm explanation documents using Markdown. The style should be:
- **Educational-focused** - Clear hierarchy and scannable content
- **Technically accurate** - Proper code formatting and examples
- **Visually consistent** - Uniform styling across all sections
- **Platform-agnostic** - Works well on GitHub, GitLab, documentation sites, etc.

---

## 📋 Document Structure Template

```markdown
# 🎯 [Algorithm Pattern Name]: Complete Guide

**[Brief subtitle or description]**

---

## 🎯 Problem Understanding
[Problem statement and context]

---

## 🔍 Why This Pattern?
[Pattern justification and comparison]

---

## ⚙️ Algorithm Deep Dive
[Core implementation details]

---

## 📊 Complete Example Walkthrough
[Step-by-step trace]

---

## 📈 Complexity Analysis
[Time/space analysis]

---

## 💡 Pro Tips & Tricks
[Practical advice]

---

## 🧪 Additional Examples & Edge Cases
[More test cases]

---

## 🔧 Optimization Techniques
[Advanced improvements]

---

## 🎓 Related Problems & Variations
[Similar patterns]

---

## 📝 Interview Preparation Checklist
[Preparation guide]

---

## 🚀 Final Code Implementation
[Complete solution]

---

## 🎯 When to Use This Pattern
[Application guidelines]

---

## 🏆 Mastery Summary
[Key takeaways]
```

---

## 🎨 Formatting Standards

### Header Hierarchy

```markdown
# 🎯 Main Title (H1) - Only one per document
## 📊 Section Title (H2) - Major sections with emoji
### Subsection Title (H3) - No emoji
#### Component Title (H4) - Specific components
```

### Emoji Usage Guidelines

**Section Icons (H2 level):**
- 🎯 Problem Understanding
- 🔍 Why This Pattern?
- ⚙️ Algorithm Deep Dive
- 📊 Complete Example / Walkthrough
- 📈 Complexity Analysis
- 💡 Pro Tips & Tricks
- 🧪 Additional Examples / Edge Cases
- 🔧 Optimization Techniques
- 🎓 Related Problems
- 📝 Interview Preparation
- 🚀 Final Implementation
- 🏆 Mastery Summary

**Content Icons (inline):**
- ✅ Success/Correct
- ❌ Error/Invalid
- 🎉 Found match/Success
- ⚠️ Warning/Caution
- 💡 Tip/Insight
- 📋 Checklist
- 🔄 Process/Flow

---

## 📊 Visual Elements

### 1. ASCII Art for Visualizations

#### String/Array Representations
```markdown
┌───┬───┬───┬───┬───┐
│bar│foo│the│foo│bar│
└───┴───┴───┴───┴───┘
 ✅  ✅  ❌  ✅  ✅
```

#### Window Representations
```markdown
Window: [bar][foo] ← current window
State: seen_words = {"bar": 1, "foo": 1}
```

#### Flow Diagrams
```markdown
Expand → Check → Shrink → Record
```

### 2. Tables for Structured Data

#### Complexity Analysis
```markdown
| Approach | Time Complexity | Space Complexity | Explanation |
|----------|----------------|------------------|-------------|
| Brute Force | O(n × m × k) | O(m) | Check every substring |
| Sliding Window | O(n × k) | O(m) | Each char visited twice |
```

#### Test Cases
```markdown
| Input | Expected | Description |
|-------|----------|-------------|
| s="abc", words=["a","b"] | [0] | Basic case |
| s="", words=["a"] | [] | Empty string |
```

### 3. Code Blocks with Language Tags

```markdown
```python
def function_name(params):
    """Docstring here."""
    # Implementation
    return result
```
```

### 4. Blockquotes for Key Insights

```markdown
> **Key Realization:** Instead of checking every possible substring, 
> we can maintain a "window" that slides through the string.

> **Word-Level Sliding:** Move in chunks of word_length instead 
> of character by character.
```

### 5. Step-by-Step Walkthroughs

```markdown
#### Step 1: Add "bar" at position 0
```
Window: [bar] ← current
State: seen_words = {"bar": 1}, matched_words = 1
```

#### Step 2: Add "foo" at position 3
```
Window: [bar][foo] ← found complete match!
State: seen_words = {"bar": 1, "foo": 1}, matched_words = 2
🎉 FOUND MATCH at position 0!
```
```

---

## 💻 Code Formatting Rules

### 1. Code Block Languages

```markdown
```python          # Python implementations
```javascript      # JavaScript implementations  
```java            # Java implementations
```cpp             # C++ implementations
```text            # Pseudocode or plain text
```bash            # Terminal commands
```
```

### 2. Inline Code

```markdown
Use `backticks` for:
- Variable names: `word_len`, `matched_words`
- Function names: `findSubstring()`, `defaultdict()`
- Short code snippets: `s[i:j]`
- File names: `sliding_window.py`
```

### 3. Code Documentation Standards

```markdown
```python
def function_name(param1, param2):
    """
    Brief description of what the function does.
    
    Args:
        param1: Description of parameter
        param2: Description of parameter
    
    Returns:
        Description of return value
    """
    # Implementation with comments
    return result
```
```

---

## 📋 Content Organization Patterns

### 1. Problem Statement Format

```markdown
### LeetCode Problem: [Problem Name]

**Given:** [Input description]  
**Find:** [Output description]  
**Example:** [Concrete example with input/output]

### Why This Problem is Tricky

- **Challenge 1:** Description
- **Challenge 2:** Description
- **Challenge 3:** Description
```

### 2. Algorithm Explanation Format

```markdown
### The [Strategy Name]

[Explanation paragraph]

#### Example: [concrete example]

```
[ASCII visualization]
```

**Result:** [outcome]
```

### 3. Tips and Tricks Format

```markdown
### 💡 [Category Name]

[Introductory paragraph]

- **Point 1:** Explanation with emphasis
- **Point 2:** Explanation with emphasis
- **Point 3:** Explanation with emphasis
```

### 4. Checklist Format

```markdown
### ✅ [Category Name]
- [ ] Item 1 description
- [ ] Item 2 description
- [ ] Item 3 description
```

---

## 🎨 Typography and Emphasis

### 1. Text Emphasis Hierarchy

```markdown
**Bold** - For important concepts, keywords, emphasis
*Italic* - For variables, mathematical terms, subtle emphasis
`Code` - For code elements, filenames, technical terms
```

### 2. List Formatting

#### Unordered Lists
```markdown
- **Primary point:** Description with bold keyword
- **Secondary point:** Description
  - Nested sub-point
  - Another sub-point
```

#### Ordered Lists
```markdown
1. **Step description:** Action to take
2. **Next step:** Following action
3. **Final step:** Concluding action
```

### 3. Link Formatting

```markdown
[Display Text](URL) - External links
[Section Reference](#header-name) - Internal links
```

---

## 📊 Visual Layout Techniques

### 1. Horizontal Rules for Separation

```markdown
---
```
Use between major sections for visual separation.

### 2. Line Breaks for Spacing

```markdown
Double line breaks for paragraph separation.

Single line breaks for  
forced line breaks within paragraphs.
```

### 3. Indentation for Hierarchy

```markdown
Main point
    Sub-point (4 spaces)
        Sub-sub-point (8 spaces)
```

---

## 🧪 Specialized Components

### 1. Example Boxes

```markdown
#### Example [N]: [Description]

```python
s = "example", words = ["ex", "am"]
# Challenge: [What makes this interesting]

Target: {"ex": 1, "am": 1}
┌──┬──┬──┐
│ex│am│pl│
└──┴──┴──┘
Result: [0] # [Explanation of result]
```
```

### 2. Edge Case Documentation

```markdown
#### [Category] Cases to Consider

##### Input Validation
- **Empty string:** s = "" → return []
- **Empty array:** words = [] → return []
- **Invalid length:** len(s) < total → return []

##### Boundary Conditions  
- **Exact match:** String length equals target
- **Single element:** Only one word to find
- **Maximum size:** Large inputs within constraints
```

### 3. Optimization Sections

```markdown
### [Optimization Category]

```python
# 1. Optimization description
if condition:
    # Optimized approach
    
# 2. Another optimization
optimization_code_here
```

**Benefits:**
- Benefit 1
- Benefit 2
```

---

## 📝 Implementation Checklist

### ✅ Document Structure
- [ ] Use the template structure with all required sections
- [ ] Include appropriate emoji icons for H2 headers
- [ ] Follow header hierarchy (H1→H2→H3→H4)
- [ ] Add horizontal rules between major sections

### ✅ Content Formatting
- [ ] Use proper code blocks with language tags
- [ ] Include ASCII art for visual examples
- [ ] Add tables for structured data (complexity, test cases)
- [ ] Use blockquotes for key insights
- [ ] Format step-by-step walkthroughs consistently

### ✅ Visual Elements
- [ ] Apply consistent emoji usage
- [ ] Use proper emphasis (bold/italic/code)
- [ ] Include visual separators (horizontal rules)
- [ ] Maintain consistent indentation
- [ ] Add appropriate spacing between sections

### ✅ Technical Content
- [ ] Include complete code implementation
- [ ] Add complexity analysis table
- [ ] Provide multiple examples with edge cases
- [ ] Include practical tips and debugging advice
- [ ] Add related problems and variations

### ✅ Polish
- [ ] Check all code blocks for proper syntax highlighting
- [ ] Verify table formatting renders correctly
- [ ] Ensure consistent spacing throughout
- [ ] Test internal links work properly
- [ ] Validate ASCII art displays correctly

---

## 🎯 Customization Guidelines

### For Different Algorithm Patterns

```markdown
# 🎯 [Pattern Name]: Complete Guide
**Master Guide for [Specific Problem/Category]**
```

### Section Icon Variations by Pattern

**Dynamic Programming:**
- 🎯 Problem Understanding
- 🔍 Why Dynamic Programming?
- ⚙️ State Design & Transitions
- 📊 Complete Example
- 📈 Complexity Analysis
- 💡 DP Tips & Tricks

**Graph Algorithms:**
- 🎯 Problem Understanding  
- 🔍 Why Graph Traversal?
- ⚙️ Graph Representation & Algorithm
- 📊 Complete Example
- 📈 Complexity Analysis
- 💡 Graph Tips & Tricks

**Tree Algorithms:**
- 🎯 Problem Understanding
- 🔍 Why Tree Traversal?
- ⚙️ Tree Structure & Algorithm  
- 📊 Complete Example
- 📈 Complexity Analysis
- 💡 Tree Tips & Tricks

### ASCII Art Adaptations

**For Arrays:**
```markdown
[0][1][2][3][4]
```

**For Trees:**
```markdown
    root
   /    \
  left  right
```

**For Graphs:**
```markdown
A --- B
|     |
C --- D
```

---

## 🚀 Quick Start Template

```markdown
# 🎯 [Algorithm Pattern]: Complete Guide

**Master Guide for [Problem Name]**

---

## 🎯 Problem Understanding

### [Platform] Problem: [Problem Title]

**Given:** [Input description]  
**Find:** [Output description]  
**Example:** [Concrete example]

### Why This Problem is Tricky

- **[Challenge 1]:** [Description]
- **[Challenge 2]:** [Description]

---

## 🔍 Why [Pattern Name]?

### Brute Force Approach (Inefficient)

```python
# Inefficient approach
```

### [Pattern] Insight

> **Key Realization:** [Main insight]

---

## ⚙️ Algorithm Deep Dive

[Algorithm explanation with code and examples]

---

## 📊 Complete Example Walkthrough

[Step-by-step trace]

---

## 📈 Complexity Analysis

| Approach | Time | Space | Explanation |
|----------|------|-------|-------------|
| Brute Force | O(?) | O(?) | [Description] |
| [Pattern] | O(?) | O(?) | [Description] |

---

## 💡 Pro Tips & Tricks

### 💡 [Category]
- **[Tip 1]:** [Description]
- **[Tip 2]:** [Description]

---

## 🚀 Final Code Implementation

```python
def solution(params):
    """
    [Docstring]
    """
    # Implementation
    return result
```

---

## 🏆 Mastery Summary

> *"[Inspirational quote about the pattern]"*

🎯 **Master the pattern, ace the interview!** 🚀
```
