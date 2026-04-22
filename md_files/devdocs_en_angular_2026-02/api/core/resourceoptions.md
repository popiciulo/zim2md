# ResourceOptions

ResourceOptions



# ResourceOptions

## API

```
type ResourceOptions<T, R> = (
  | PromiseResourceOptions<T, R>
  | StreamingResourceOptions<T, R>
) & {
  /**
   * A debug name for the reactive node. Used in Angular DevTools to identify the node.
   */
  debugName?: string;
}
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/ResourceOptions>
