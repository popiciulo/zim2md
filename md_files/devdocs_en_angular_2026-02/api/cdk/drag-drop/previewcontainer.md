# PreviewContainer

PreviewContainer



# PreviewContainer

Possible places into which the preview of a drag item can be inserted.

- `global` - Preview will be inserted at the bottom of the `<body>`. The advantage is that you don't have to worry about `overflow: hidden` or `z-index`, but the item won't retain its inherited styles.
- `parent` - Preview will be inserted into the parent of the drag item. The advantage is that inherited styles will be preserved, but it may be clipped by `overflow: hidden` or not be visible due to `z-index`. Furthermore, the preview is going to have an effect over selectors like `:nth-child` and some flexbox configurations.
- `ElementRef<HTMLElement> | HTMLElement` - Preview will be inserted into a specific element. Same advantages and disadvantages as `parent`.

## API

```
type PreviewContainer = 'global' | 'parent' | ElementRef<HTMLElement> | HTMLElement
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/cdk/drag-drop/PreviewContainer>
