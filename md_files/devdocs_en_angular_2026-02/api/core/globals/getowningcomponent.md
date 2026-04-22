# getOwningComponent

getOwningComponent



# getOwningComponent

Retrieves the component instance whose view contains the DOM element.

## API

```
function getOwningComponent<T>(elementOrDir: {} | Element): T | null;
```

### getOwningComponent

`T | null`

Retrieves the component instance whose view contains the DOM element.

For example, if `<child-comp>` is used in the template of `<app-comp>` (i.e. a `ViewChild` of `<app-comp>`), calling [`getOwningComponent`](getowningcomponent) on `<child-comp>` would return `<app-comp>`.

@paramelementOrDir`{} | Element`

DOM element, component or directive instance for which to retrieve the root components.

@returns`T | null`

## Description

Retrieves the component instance whose view contains the DOM element.

For example, if `<child-comp>` is used in the template of `<app-comp>` (i.e. a `ViewChild` of `<app-comp>`), calling [`getOwningComponent`](getowningcomponent) on `<child-comp>` would return `<app-comp>`.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/globals/getOwningComponent>
