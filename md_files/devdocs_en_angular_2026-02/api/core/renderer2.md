# Renderer2

Renderer2



# Renderer2

Extend this base class to implement custom rendering. By default, Angular renders a template into DOM. You can use custom rendering to intercept rendering calls, or to render to something other than DOM.

## API

```
abstract class Renderer2 {
  abstract readonly data: { [key: string]: any; };
  abstract destroy(): void;
  abstract createElement(name: string, namespace?: string | null | undefined): any;
  abstract createComment(value: string): any;
  abstract createText(value: string): any;
  destroyNode: ((node: any) => void) | null;
  abstract appendChild(parent: any, newChild: any): void;
  abstract insertBefore(parent: any, newChild: any, refChild: any, isMove?: boolean | undefined): void;
  abstract removeChild(parent: any, oldChild: any, isHostElement?: boolean | undefined, requireSynchronousElementRemoval?: boolean | undefined): void;
  abstract selectRootElement(selectorOrNode: any, preserveContent?: boolean | undefined): any;
  abstract parentNode(node: any): any;
  abstract nextSibling(node: any): any;
  abstract setAttribute(el: any, name: string, value: string, namespace?: string | null | undefined): void;
  abstract removeAttribute(el: any, name: string, namespace?: string | null | undefined): void;
  abstract addClass(el: any, name: string): void;
  abstract removeClass(el: any, name: string): void;
  abstract setStyle(el: any, style: string, value: any, flags?: RendererStyleFlags2 | undefined): void;
  abstract removeStyle(el: any, style: string, flags?: RendererStyleFlags2 | undefined): void;
  abstract setProperty(el: any, name: string, value: any): void;
  abstract setValue(node: any, value: string): void;
  abstract listen(target: any, eventName: string, callback: (event: any) => boolean | void, options?: ListenerOptions | undefined): () => void;
}
```

### data

`{ [key: string]: any; }`

Use to store arbitrary developer-defined data on a renderer instance, as an object containing key-value pairs. This is useful for renderers that delegate to other renderers.

### destroy

`void`

Implement this callback to destroy the renderer or the host element.

@returns`void`

### createElement

`any`

Implement this callback to create an instance of the host element.

@paramname`string`

An identifying name for the new element, unique within the namespace.

@paramnamespace`string | null | undefined`

The namespace for the new element.

@returns`any`

### createComment

`any`

Implement this callback to add a comment to the DOM of the host element.

@paramvalue`string`

The comment text.

@returns`any`

### createText

`any`

Implement this callback to add text to the DOM of the host element.

@paramvalue`string`

The text string.

@returns`any`

### destroyNode

`((node: any) => void) | null`

If null or undefined, the view engine won't call it. This is used as a performance optimization for production mode.

### appendChild

`void`

Appends a child to a given parent node in the host element DOM.

@paramparent`any`

The parent node.

@paramnewChild`any`

The new child node.

@returns`void`

### insertBefore

`void`

Implement this callback to insert a child node at a given position in a parent node in the host element DOM.

@paramparent`any`

The parent node.

@paramnewChild`any`

The new child nodes.

@paramrefChild`any`

The existing child node before which `newChild` is inserted.

@paramisMove`boolean | undefined`

Optional argument which signifies if the current `insertBefore` is a result of a move. Animation uses this information to trigger move animations. In the past the Animation would always assume that any `insertBefore` is a move. This is not strictly true because with runtime i18n it is possible to invoke `insertBefore` as a result of i18n and it should not trigger an animation move.

@returns`void`

### removeChild

`void`

Implement this callback to remove a child node from the host element's DOM.

@paramparent`any`

The parent node.

@paramoldChild`any`

The child node to remove.

@paramisHostElement`boolean | undefined`

Optionally signal to the renderer whether this element is a host element

@paramrequireSynchronousElementRemoval`boolean | undefined`

Optionally signal to the renderer whether this element needs synchronous removal

@returns`void`

### selectRootElement

`any`

Implement this callback to prepare an element to be bootstrapped as a root element, and return the element instance.

@paramselectorOrNode`any`

The DOM element.

@parampreserveContent`boolean | undefined`

Whether the contents of the root element should be preserved, or cleared upon bootstrap (default behavior). Use with [`ViewEncapsulation.ShadowDom`](viewencapsulation#ShadowDom) to allow simple native content projection via `<slot>` elements.

@returns`any`

### parentNode

`any`

Implement this callback to get the parent of a given node in the host element's DOM.

@paramnode`any`

The child node to query.

@returns`any`

### nextSibling

`any`

Implement this callback to get the next sibling node of a given node in the host element's DOM.

@paramnode`any`

@returns`any`

### setAttribute

`void`

Implement this callback to set an attribute value for an element in the DOM.

@paramel`any`

The element.

@paramname`string`

The attribute name.

@paramvalue`string`

The new value.

@paramnamespace`string | null | undefined`

The namespace.

@returns`void`

### removeAttribute

`void`

Implement this callback to remove an attribute from an element in the DOM.

@paramel`any`

The element.

@paramname`string`

The attribute name.

@paramnamespace`string | null | undefined`

The namespace.

@returns`void`

### addClass

`void`

Implement this callback to add a class to an element in the DOM.

@paramel`any`

The element.

@paramname`string`

The class name.

@returns`void`

### removeClass

`void`

Implement this callback to remove a class from an element in the DOM.

@paramel`any`

The element.

@paramname`string`

The class name.

@returns`void`

### setStyle

`void`

Implement this callback to set a CSS style for an element in the DOM.

@paramel`any`

The element.

@paramstyle`string`

The name of the style.

@paramvalue`any`

The new value.

@paramflags`RendererStyleFlags2 | undefined`

Flags for style variations. No flags are set by default.

@returns`void`

### removeStyle

`void`

Implement this callback to remove the value from a CSS style for an element in the DOM.

@paramel`any`

The element.

@paramstyle`string`

The name of the style.

@paramflags`RendererStyleFlags2 | undefined`

Flags for style variations to remove, if set. ???

@returns`void`

### setProperty

`void`

Implement this callback to set the value of a property of an element in the DOM.

@paramel`any`

The element.

@paramname`string`

The property name.

@paramvalue`any`

The new value.

@returns`void`

### setValue

`void`

Implement this callback to set the value of a node in the host element.

@paramnode`any`

The node.

@paramvalue`string`

The new value.

@returns`void`

### listen

`() => void`

Implement this callback to start an event listener.

@paramtarget`any`

The context in which to listen for events. Can be the entire window or document, the body of the document, or a specific DOM element.

@parameventName`string`

The event to listen for.

@paramcallback`(event: any) => boolean | void`

A handler function to invoke when the event occurs.

@paramoptions`ListenerOptions | undefined`

Options that configure how the event listener is bound.

@returns`() => void`

## Description

Extend this base class to implement custom rendering. By default, Angular renders a template into DOM. You can use custom rendering to intercept rendering calls, or to render to something other than DOM.

Please be aware that usage of `Renderer2`, in context of accessing DOM elements, provides no extra security which makes it equivalent to [`Security vulnerabilities`](https://angular.dev/best-practices/security#direct-use-of-the-dom-apis-and-explicit-sanitization-calls).

Create your custom renderer using [`RendererFactory2`](rendererfactory2).

Use a custom renderer to bypass Angular's templating and make custom UI changes that can't be expressed declaratively. For example if you need to set a property or an attribute whose name is not statically known, use the `setProperty()` or `setAttribute()` method.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/Renderer2>
