# HTML Style Guide for Algorithm Explanation Pages

## 🎨 Design Philosophy

Create **visually engaging, educational, and professional** algorithm explanation pages that combine modern web design with clear technical content. The style should be:
- **Premium and cutting-edge** - Modern gradients, shadows, and animations
- **Educational-focused** - Clear hierarchy and scannable content
- **Technically accurate** - Proper code formatting and examples
- **Visually consistent** - Uniform styling across all sections

## 📋 HTML Structure Template

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>[Algorithm Pattern]: [Problem Name]</title>
    <style>
        /* CSS goes here */
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🎯 [Algorithm Pattern Name]</h1>
            <p>[Brief description or subtitle]</p>
        </div>

        <div class="content-card">
            <!-- Sections go here -->
        </div>
    </div>
</body>
</html>
```

## 🎨 Color Palette & Theme

### Primary Colors
- **Background Gradient**: `linear-gradient(135deg, #667eea 0%, #764ba2 100%)`
- **Primary Blue**: `#667eea` 
- **Primary Purple**: `#764ba2`
- **Text Dark**: `#2c3e50`
- **Text Light**: `#718096`

### Semantic Colors
- **Success/Valid**: `#38a169` (green)
- **Error/Invalid**: `#e53e3e` (red) 
- **Warning/Info**: `#f59e0b` (amber)
- **Code Background**: `#2d3748` (dark gray)
- **Code Text**: `#e2e8f0` (light gray)

### Neutral Colors
- **Card Background**: `white`
- **Section Background**: `#f8f9fa`
- **Border Color**: `#e2e8f0`
- **Light Background**: `#f7fafc`

## 🏗️ CSS Architecture

### Base Styles
```css
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    line-height: 1.6;
    color: #333;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    min-height: 100vh;
}
```

### Container Structure
```css
.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
}

.content-card {
    background: white;
    border-radius: 15px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    overflow: hidden;
    margin-bottom: 30px;
}
```

## 📑 Section Components

### 1. Header Component
```css
.header {
    text-align: center;
    color: white;
    margin-bottom: 30px;
}

.header h1 {
    font-size: 2.5em;
    margin-bottom: 10px;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
}

.header p {
    font-size: 1.2em;
    opacity: 0.9;
}
```

### 2. Section Layout
```css
.section {
    padding: 30px;
    border-bottom: 1px solid #eee;
}

.section:last-child {
    border-bottom: none;
}

.section-title {
    font-size: 1.8em;
    color: #2c3e50;
    margin-bottom: 20px;
    display: flex;
    align-items: center;
    gap: 10px;
}

.section-title::before {
    content: '';
    width: 4px;
    height: 30px;
    background: linear-gradient(135deg, #667eea, #764ba2);
    border-radius: 2px;
}
```

### 3. Subsection Component
```css
.subsection {
    margin: 25px 0;
    padding: 20px;
    background: #f8f9fa;
    border-radius: 10px;
    border-left: 4px solid #667eea;
}

.subsection h3 {
    color: #2c3e50;
    margin-bottom: 15px;
    font-size: 1.3em;
}
```

## 💻 Code Block Styling

### Main Code Block
```css
.code-block {
    background: #2d3748;
    color: #e2e8f0;
    padding: 20px;
    border-radius: 8px;
    margin: 15px 0;
    overflow-x: auto;
    font-family: 'Courier New', monospace;
    font-size: 14px;
    white-space: pre;
    line-height: 1.5;
    tab-size: 4;
}

.code-block .comment { color: #68d391; }
.code-block .keyword { color: #f093fb; }
.code-block .string { color: #fbb6ce; }
```

## 🎯 Visual Components

### 1. Visual Examples
```css
.visual-example {
    background: #f7fafc;
    border: 2px solid #e2e8f0;
    border-radius: 10px;
    padding: 20px;
    margin: 20px 0;
}

.string-display {
    font-family: 'Courier New', monospace;
    font-size: 16px;
    margin: 15px 0;
}
```

### 2. Word Chunks (for algorithm visualization)
```css
.word-chunk {
    display: inline-block;
    padding: 8px 12px;
    margin: 3px;
    border: 2px solid #cbd5e0;
    border-radius: 6px;
    background: #f7fafc;
    min-width: 40px;
    text-align: center;
    transition: all 0.3s ease;
}

.word-chunk:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}

/* Semantic variations */
.valid-word { background: #c6f6d5; border-color: #38a169; color: #22543d; }
.invalid-word { background: #fed7d7; border-color: #e53e3e; color: #742a2a; text-decoration: line-through; }
.current-window { background: #bee3f8; border-color: #3182ce; color: #2a4365; border-width: 3px; }
.found-match { background: #c6f6d5; border-color: #38a169; color: #22543d; border-width: 3px; box-shadow: 0 0 10px rgba(56, 161, 105, 0.3); }
```

### 3. Step-by-Step Components
```css
.step {
    display: flex;
    align-items: flex-start;
    margin: 20px 0;
    padding: 15px;
    background: white;
    border-radius: 8px;
    border: 1px solid #e2e8f0;
}

.step-counter {
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: white;
    width: 30px;
    height: 30px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: bold;
    margin-right: 15px;
    flex-shrink: 0;
}
```

## 📊 Specialized Components

### 1. Highlight Boxes
```css
.highlight-box {
    background: linear-gradient(135deg, #667eea10, #764ba210);
    border: 1px solid #667eea;
    border-radius: 8px;
    padding: 20px;
    margin: 20px 0;
}
```

### 2. Tip Boxes
```css
.tip-box {
    background: #fffbeb;
    border: 1px solid #f59e0b;
    border-radius: 8px;
    padding: 20px;
    margin: 20px 0;
    border-left: 4px solid #f59e0b;
}

.tip-box h4 {
    color: #92400e;
    margin-bottom: 10px;
    display: flex;
    align-items: center;
    gap: 8px;
}

.tip-box h4::before {
    content: "💡";
}
```

### 3. Problem Statement Box
```css
.problem-statement {
    background: #e6fffa;
    border: 1px solid #38b2ac;
    border-radius: 8px;
    padding: 20px;
    margin: 20px 0;
}

.problem-statement h3 {
    color: #234e52;
    margin-bottom: 15px;
}
```

### 4. Tables
```css
.complexity-table {
    width: 100%;
    border-collapse: collapse;
    margin: 20px 0;
}

.complexity-table th,
.complexity-table td {
    border: 1px solid #e2e8f0;
    padding: 12px;
    text-align: left;
}

.complexity-table th {
    background: #f7fafc;
    font-weight: bold;
    color: #2d3748;
}

.complexity-table tr:nth-child(even) {
    background: #f9f9f9;
}
```

### 5. Algorithm Flow
```css
.algorithm-flow {
    display: flex;
    flex-wrap: wrap;
    gap: 15px;
    margin: 20px 0;
}

.flow-step {
    flex: 1;
    min-width: 200px;
    padding: 15px;
    background: #f7fafc;
    border: 2px solid #e2e8f0;
    border-radius: 8px;
    text-align: center;
    position: relative;
}

.flow-step::after {
    content: "→";
    position: absolute;
    right: -25px;
    top: 50%;
    transform: translateY(-50%);
    font-size: 20px;
    color: #667eea;
    font-weight: bold;
}

.flow-step:last-child::after {
    display: none;
}
```

## 📝 Content Structure Guidelines

### 1. Required Sections (in order)
1. **Problem Understanding** - What we're solving
2. **Why This Pattern?** - Pattern justification  
3. **Algorithm Deep Dive** - Core implementation
4. **Complete Example** - Step-by-step walkthrough
5. **Complexity Analysis** - Time/space analysis
6. **Pro Tips & Tricks** - Practical advice
7. **Edge Cases** - Additional examples
8. **Optimization Techniques** - Advanced improvements
9. **Related Problems** - Similar patterns
10. **Interview Preparation** - Checklist
11. **Mastery Summary** - Key takeaways

### 2. Section Emoji Icons
- 🎯 Problem Understanding
- 🔍 Why This Pattern?
- ⚙️ Algorithm Deep Dive
- 📊 Complete Example  
- 📈 Complexity Analysis
- 💡 Pro Tips & Tricks
- 🧪 Edge Cases
- 🔧 Optimization Techniques
- 🎓 Related Problems
- 📝 Interview Preparation
- 🏆 Mastery Summary

### 3. Content Hierarchy
```
h1 (Header) → h2 (Section Title) → h3 (Subsection) → h4 (Component Title)
```

## 🎨 Typography Rules

### Font Hierarchy
- **Headers**: `'Segoe UI', Tahoma, Geneva, Verdana, sans-serif`
- **Code**: `'Courier New', monospace`
- **Body**: `'Segoe UI', Tahoma, Geneva, Verdana, sans-serif`

### Font Sizes
- **H1**: `2.5em` (header)
- **H2**: `1.8em` (section titles)
- **H3**: `1.3em` (subsections)
- **H4**: `1.1em` (components)
- **Body**: `16px` (default)
- **Code**: `14px`

### Line Heights
- **Body**: `1.6`
- **Code**: `1.5`
- **Headers**: `1.2`

## 📱 Responsive Design

### Breakpoints
```css
/* Mobile */
@media (max-width: 768px) {
    .container { padding: 10px; }
    .header h1 { font-size: 2em; }
    .algorithm-flow { flex-direction: column; }
    .flow-step::after { display: none; }
}
```

## 🎯 Interactive Elements

### Hover Effects
```css
.word-chunk:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}

.step:hover {
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}
```

## 📋 Implementation Checklist

When creating a new algorithm explanation page:

### ✅ Structure
- [ ] Use the HTML template structure
- [ ] Include all required sections in order
- [ ] Add appropriate emoji icons to section titles
- [ ] Follow the content hierarchy (h1→h2→h3→h4)

### ✅ Styling
- [ ] Apply the base CSS architecture
- [ ] Use the defined color palette consistently
- [ ] Include proper code block formatting
- [ ] Add visual components for algorithm demonstration
- [ ] Implement step-by-step components where needed

### ✅ Content
- [ ] Start with clear problem statement
- [ ] Include visual examples with proper styling
- [ ] Add code implementations with syntax highlighting
- [ ] Provide complexity analysis
- [ ] Include practical tips and edge cases
- [ ] End with mastery summary

### ✅ Polish
- [ ] Test responsive design on mobile
- [ ] Verify all hover effects work
- [ ] Ensure proper spacing and alignment
- [ ] Check color contrast for accessibility
- [ ] Validate HTML structure

## 🎨 Customization Guidelines

### For Different Algorithm Patterns
- **Change the primary gradient** while keeping the structure
- **Adjust word-chunk styling** based on algorithm visualization needs
- **Modify step components** to match the algorithm's phases
- **Adapt visual examples** to the specific problem domain

### Color Scheme Variations
- **Dynamic Programming**: Green gradient (`#10b981` to `#059669`)
- **Graph Algorithms**: Blue gradient (`#3b82f6` to `#1d4ed8`)  
- **Tree Algorithms**: Purple gradient (`#8b5cf6` to `#7c3aed`)
- **Array/String**: Orange gradient (`#f59e0b` to `#d97706`)
