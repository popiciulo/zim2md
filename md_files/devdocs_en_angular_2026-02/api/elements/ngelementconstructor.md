# NgElementConstructor

NgElementConstructor



# NgElementConstructor

Prototype for a class constructor based on an Angular component that can be used for custom element registration. Implemented and returned by the [`createCustomElement() function`](createcustomelement).

[Angular Elements Overview](../../guide/elements "Turning Angular components into custom elements")

## API

```
interface NgElementConstructor<P> {
  readonly observedAttributes: string[];
}
```

### observedAttributes

`string[]`

An array of observed attribute names for the custom element, derived by transforming input property names from the source component.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/elements/NgElementConstructor>
