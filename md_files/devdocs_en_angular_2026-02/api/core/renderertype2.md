# RendererType2

RendererType2



# RendererType2

Used by [`RendererFactory2`](rendererfactory2) to associate custom rendering data and styles with a rendering implementation.

## API

```
interface RendererType2 {
  id: string;
  encapsulation: ViewEncapsulation;
  styles: string[];
  data: { [kind: string]: any; };
  getExternalStyles?: ((encapsulationId?: string | undefined) => string[]) | null | undefined;
}
```

### id

`string`

A unique identifying string for the new renderer, used when creating unique styles for encapsulation.

### encapsulation

`ViewEncapsulation`

The view encapsulation type, which determines how styles are applied to DOM elements. One of

- `Emulated` (default): Emulate native scoping of styles.
- `Native`: Use the native encapsulation mechanism of the renderer.
- `ShadowDom`: Use modern [Shadow DOM](https://w3c.github.io/webcomponents/spec/shadow/) and create a ShadowRoot for component's host element.
- `None`: Do not provide any template or style encapsulation.

### styles

`string[]`

Defines CSS styles to be stored on a renderer instance.

### data

`{ [kind: string]: any; }`

Defines arbitrary developer-defined data to be stored on a renderer instance. This is useful for renderers that delegate to other renderers.

### getExternalStyles

`((encapsulationId?: string | undefined) => string[]) | null | undefined`

A function used by the framework to create the list of external runtime style URLs.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/RendererType2>
