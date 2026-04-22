# getListeners

getListeners



# getListeners

Retrieves a list of event listeners associated with a DOM element. The list does include host listeners, but it does not include event listeners defined outside of the Angular context (e.g. through `addEventListener`).

## API

```
function getListeners(element: Element): Listener[];
```

### getListeners

`Listener[]`

Retrieves a list of event listeners associated with a DOM element. The list does include host listeners, but it does not include event listeners defined outside of the Angular context (e.g. through `addEventListener`).

@paramelement`Element`

Element for which the DOM listeners should be retrieved.

@returns`Listener[]`

Usage notes

Given the following DOM structure:

```
<app-root>
  <div (click)="doSomething()"></div>
</app-root>
```

Calling [`getListeners`](getlisteners) on `<div>` will return an object that looks as follows:

```
{
  name: 'click',
  element: <div>,
  callback: () => doSomething(),
  useCapture: false
}
```

## Usage Notes

Given the following DOM structure:

```
<app-root>
  <div (click)="doSomething()"></div>
</app-root>
```

Calling [`getListeners`](getlisteners) on `<div>` will return an object that looks as follows:

```
{
  name: 'click',
  element: <div>,
  callback: () => doSomething(),
  useCapture: false
}
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/globals/getListeners>
