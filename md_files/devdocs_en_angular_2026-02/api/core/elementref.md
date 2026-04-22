# ElementRef

ElementRef



# ElementRef

A wrapper around a native element inside of a View.

[Using DOM APIs](../../guide/components/dom-apis)

## API

```
class ElementRef<T = any> {
  constructor(nativeElement: T): ElementRef<T>;
  nativeElement: T;
}
```

### constructor

`ElementRef<T>`

@paramnativeElement`T`

@returns`ElementRef<T>`

### nativeElement

`T`

Use with caution

Use this API as the last resort when direct access to DOM is needed. Use templating and data-binding provided by Angular instead. If used, it is recommended in combination with [`DomSanitizer`](https://angular.dev/best-practices/security#direct-use-of-the-dom-apis-and-explicit-sanitization-calls) for maxiumum security;

## Description

A wrapper around a native element inside of a View.

An [`ElementRef`](elementref) is backed by a render-specific element. In the browser, this is usually a DOM element.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/ElementRef>
