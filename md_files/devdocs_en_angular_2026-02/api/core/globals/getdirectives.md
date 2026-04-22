# getDirectives

getDirectives



# getDirectives

Retrieves directive instances associated with a given DOM node. Does not include component instances.

## API

```
function getDirectives(node: Node): {}[];
```

### getDirectives

`{}[]`

Retrieves directive instances associated with a given DOM node. Does not include component instances.

@paramnode`Node`

DOM node for which to get the directives.

@returns`{}[]`

Usage notes

Given the following DOM structure:

```
<app-root>
  <button my-button></button>
  <my-comp></my-comp>
</app-root>
```

Calling [`getDirectives`](getdirectives) on `<button>` will return an array with an instance of the `MyButton` directive that is associated with the DOM node.

Calling [`getDirectives`](getdirectives) on `<my-comp>` will return an empty array.

## Usage Notes

Given the following DOM structure:

```
<app-root>
  <button my-button></button>
  <my-comp></my-comp>
</app-root>
```

Calling [`getDirectives`](getdirectives) on `<button>` will return an array with an instance of the `MyButton` directive that is associated with the DOM node.

Calling [`getDirectives`](getdirectives) on `<my-comp>` will return an empty array.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/globals/getDirectives>
