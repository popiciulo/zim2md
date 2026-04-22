# getContext

getContext



# getContext

If inside an embedded view (e.g. `*ngIf` or `*ngFor`), retrieves the context of the embedded view that the element is part of. Otherwise retrieves the instance of the component whose view owns the element (in this case, the result is the same as calling [`getOwningComponent`](getowningcomponent)).

## API

```
function getContext<T extends {}>(element: Element): T | null;
```

### getContext

`T | null`

If inside an embedded view (e.g. `*ngIf` or `*ngFor`), retrieves the context of the embedded view that the element is part of. Otherwise retrieves the instance of the component whose view owns the element (in this case, the result is the same as calling [`getOwningComponent`](getowningcomponent)).

@paramelement`Element`

Element for which to get the surrounding component instance.

@returns`T | null`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/globals/getContext>
