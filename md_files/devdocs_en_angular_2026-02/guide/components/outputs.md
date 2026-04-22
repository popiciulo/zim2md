# Custom events with outputs

Custom events with outputs



# Custom events with outputs

  

**TIP:** This guide assumes you've already read the [Essentials Guide](https://angular.dev/essentials). Read that first if you're new to Angular.

Angular components can define custom events by assigning a property to the [`output`](../../api/core/output) function:

```
@Component({/*...*/})
export class ExpandablePanel {
  panelClosed = output<void>();
}
```

```
<expandable-panel (panelClosed)="savePanelState()" />
```

The [`output`](../../api/core/output) function returns an [`OutputEmitterRef`](../../api/core/outputemitterref). You can emit an event by calling the `emit` method on the [`OutputEmitterRef`](../../api/core/outputemitterref):

```
  this.panelClosed.emit();
```

Angular refers to properties initialized with the [`output`](../../api/core/output) function as **outputs**. You can use outputs to raise custom events, similar to native browser events like `click`.

**Angular custom events do not bubble up the DOM**.

**Output names are case-sensitive.**

When extending a component class, **outputs are inherited by the child class.**

The [`output`](../../api/core/output) function has special meaning to the Angular compiler. **You can exclusively call [`output`](../../api/core/output) in component and directive property initializers.**

## Emitting event data

You can pass event data when calling `emit`:

```
// You can emit primitive values.
this.valueChanged.emit(7);

// You can emit custom event objects
this.thumbDropped.emit({
  pointerX: 123,
  pointerY: 456,
})
```

When defining an event listener in a template, you can access the event data from the `$event` variable:

```
<custom-slider (valueChanged)="logValue($event)" />
```

Receive the event data in the parent component:

```
@Component({
 /*...*/
})
export class App {
  logValue(value: number) {
    ...
  }
}
```

## Customizing output names

The [`output`](../../api/core/output) function accepts a parameter that lets you specify a different name for the event in a template:

```
@Component({/*...*/})
export class CustomSlider {
  changed = output({alias: 'valueChanged'});
}
```

```
<custom-slider (valueChanged)="saveVolume()" />
```

This alias does not affect usage of the property in TypeScript code.

While you should generally avoid aliasing outputs for components, this feature can be useful for renaming properties while preserving an alias for the original name or for avoiding collisions with the name of native DOM events.

## Subscribing to outputs programmatically

When creating a component dynamically, you can programmatically subscribe to output events from the component instance. The [`OutputRef`](../../api/core/outputref) type includes a `subscribe` method:

```
const someComponentRef: ComponentRef<SomeComponent> = viewContainerRef.createComponent(/*...*/);

someComponentRef.instance.someEventProperty.subscribe(eventData => {
  console.log(eventData);
});
```

Angular automatically cleans up event subscriptions when it destroys components with subscribers. Alternatively, you can manually unsubscribe from an event. The `subscribe` function returns an [`OutputRefSubscription`](../../api/core/outputrefsubscription) with an `unsubscribe` method:

```
const eventSubscription = someComponent.someEventProperty.subscribe(eventData => {
  console.log(eventData);
});

// ...

eventSubscription.unsubscribe();
```

## Choosing event names

Avoid choosing output names that collide with events on DOM elements like HTMLElement. Name collisions introduce confusion about whether the bound property belongs to the component or the DOM element.

Avoid adding prefixes for component outputs like you would with component selectors. Since a given element can only host one component, any custom properties can be assumed to belong to the component.

Always use [camelCase](https://en.wikipedia.org/wiki/Camel_case) output names. Avoid prefixing output names with "on".

## Using outputs with RxJS

See [RxJS interop with component and directive outputs](https://angular.dev/ecosystem/rxjs-interop/output-interop) for details on interoperability between outputs and RxJS.

## Declaring outputs with the @Output decorator

**TIP:** While the Angular team recommends using the [`output`](../../api/core/output) function for new projects, the original decorator-based [`@Output`](../../api/core/output) API remains fully supported.

You can alternatively define custom events by assigning a property to a new [`EventEmitter`](../../api/core/eventemitter) and adding the [`@Output`](../../api/core/output) decorator:

```
@Component({/*...*/})
export class ExpandablePanel {
  @Output() panelClosed = new EventEmitter<void>();
}
```

You can emit an event by calling the `emit` method on the [`EventEmitter`](../../api/core/eventemitter).

### Aliases with the @Output decorator

The [`@Output`](../../api/core/output) decorator accepts a parameter that lets you specify a different name for the event in a template:

```
@Component({/*...*/})
export class CustomSlider {
  @Output('valueChanged') changed = new EventEmitter<number>();
}
```

```
<custom-slider (valueChanged)="saveVolume()" />
```

This alias does not affect usage of the property in TypeScript code.

## Specify outputs in the @Component decorator

In addition to the [`@Output`](../../api/core/output) decorator, you can also specify a component's outputs with the `outputs` property in the [`@Component`](../../api/core/component) decorator. This can be useful when a component inherits a property from a base class:

```
// `CustomSlider` inherits the `valueChanged` property from `BaseSlider`.
@Component({
  /*...*/
  outputs: ['valueChanged'],
})
export class CustomSlider extends BaseSlider {}
```

You can additionally specify an output alias in the `outputs` list by putting the alias after a colon in the string:

```
// `CustomSlider` inherits the `valueChanged` property from `BaseSlider`.
@Component({
  /*...*/
  outputs: ['valueChanged: volumeChanged'],
})
export class CustomSlider extends BaseSlider {}
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/guide/components/outputs>
