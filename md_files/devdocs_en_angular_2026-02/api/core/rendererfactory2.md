# RendererFactory2

RendererFactory2



# RendererFactory2

Creates and initializes a custom renderer that implements the [`Renderer2`](renderer2) base class.

## API

```
abstract class RendererFactory2 {
  abstract createRenderer(hostElement: any, type: RendererType2 | null): Renderer2;
  abstract optional begin(): void;
  abstract optional end(): void;
  abstract optional whenRenderingDone(): Promise<any>;
}
```

### createRenderer

`Renderer2`

Creates and initializes a custom renderer for a host DOM element.

@paramhostElement`any`

The element to render.

@paramtype`RendererType2 | null`

The base class to implement.

@returns`Renderer2`

### begin

`void`

A callback invoked when rendering has begun.

@returns`void`

### end

`void`

A callback invoked when rendering has completed.

@returns`void`

### whenRenderingDone

`Promise<any>`

Use with animations test-only mode. Notifies the test when rendering has completed.

@returns`Promise<any>`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/RendererFactory2>
