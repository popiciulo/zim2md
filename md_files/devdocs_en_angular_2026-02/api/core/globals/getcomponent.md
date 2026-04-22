# getComponent

getComponent



# getComponent

Retrieves the component instance associated with a given DOM element.

## API

```
function getComponent<T>(element: Element): T | null;
```

### getComponent

`T | null`

Retrieves the component instance associated with a given DOM element.

@paramelement`Element`

DOM element from which the component should be retrieved.

@returns`T | null`

Usage notes

Given the following DOM structure:

```
<app-root>
  <div>
    <child-comp></child-comp>
  </div>
</app-root>
```

Calling [`getComponent`](getcomponent) on `<child-comp>` will return the instance of `ChildComponent` associated with this DOM element.

Calling the function on `<app-root>` will return the `MyApp` instance.

## Usage Notes

Given the following DOM structure:

```
<app-root>
  <div>
    <child-comp></child-comp>
  </div>
</app-root>
```

Calling [`getComponent`](getcomponent) on `<child-comp>` will return the instance of `ChildComponent` associated with this DOM element.

Calling the function on `<app-root>` will return the `MyApp` instance.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/globals/getComponent>
