# EventManager

EventManager



# EventManager

An injectable service that provides event management for Angular through a browser plug-in.

## API

```
class EventManager {
  constructor(plugins: EventManagerPlugin[], _zone: NgZone): EventManager;
  addEventListener(element: HTMLElement, eventName: string, handler: Function, options?: ListenerOptions | undefined): Function;
  getZone(): NgZone;
}
```

### constructor

`EventManager`

Initializes an instance of the event-manager service.

@paramplugins`EventManagerPlugin[]`

@param\_zone`NgZone`

@returns`EventManager`

### addEventListener

`Function`

Registers a handler for a specific element and event.

@paramelement`HTMLElement`

The HTML element to receive event notifications.

@parameventName`string`

The name of the event to listen for.

@paramhandler`Function`

A function to call when the notification occurs. Receives the event object as an argument.

@paramoptions`ListenerOptions | undefined`

Options that configure how the event listener is bound.

@returns`Function`

### getZone

`NgZone`

Retrieves the compilation zone in which event listeners are registered.

@returns`NgZone`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/platform-browser/EventManager>
