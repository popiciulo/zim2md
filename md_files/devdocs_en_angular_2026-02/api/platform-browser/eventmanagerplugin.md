# EventManagerPlugin

EventManagerPlugin



# EventManagerPlugin

The plugin definition for the [`EventManager`](eventmanager) class

[Extend event handling](../../guide/templates/event-listeners#extend-event-handling)

## API

```
abstract class EventManagerPlugin {
  constructor(_doc: any): EventManagerPlugin;
  manager: EventManager;
  abstract supports(eventName: string): boolean;
  abstract addEventListener(element: HTMLElement, eventName: string, handler: Function, options?: ListenerOptions | undefined): Function;
}
```

### constructor

`EventManagerPlugin`

@param\_doc`any`

@returns`EventManagerPlugin`

### manager

`EventManager`

### supports

`boolean`

Should return `true` for every event name that should be supported by this plugin

@parameventName`string`

@returns`boolean`

### addEventListener

`Function`

Implement the behaviour for the supported events

@paramelement`HTMLElement`

@parameventName`string`

@paramhandler`Function`

@paramoptions`ListenerOptions | undefined`

@returns`Function`

## Description

The plugin definition for the [`EventManager`](eventmanager) class

It can be used as a base class to create custom manager plugins, i.e. you can create your own class that extends the [`EventManagerPlugin`](eventmanagerplugin) one.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/platform-browser/EventManagerPlugin>
