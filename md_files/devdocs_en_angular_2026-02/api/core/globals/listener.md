# Listener

Listener



# Listener

Event listener configuration returned from [`getListeners`](getlisteners).

## API

```
interface Listener {
  name: string;
  element: Element;
  callback: (value: any) => any;
  useCapture: boolean;
  type: "dom" | "output";
}
```

### name

`string`

Name of the event listener.

### element

`Element`

Element that the listener is bound to.

### callback

`(value: any) => any`

Callback that is invoked when the event is triggered.

### useCapture

`boolean`

Whether the listener is using event capturing.

### type

`"dom" | "output"`

Type of the listener (e.g. a native DOM event or a custom @Output).

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/globals/Listener>
