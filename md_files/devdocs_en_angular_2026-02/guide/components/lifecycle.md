# Component Lifecycle

Component Lifecycle



# Component Lifecycle

  

**TIP:** This guide assumes you've already read the [Essentials Guide](https://angular.dev/essentials). Read that first if you're new to Angular.

A component's **lifecycle** is the sequence of steps that happen between the component's creation and its destruction. Each step represents a different part of Angular's process for rendering components and checking them for updates over time.

In your components, you can implement **lifecycle hooks** to run code during these steps. Lifecycle hooks that relate to a specific component instance are implemented as methods on your component class. Lifecycle hooks that relate the Angular application as a whole are implemented as functions that accept a callback.

A component's lifecycle is tightly connected to how Angular checks your components for changes over time. For the purposes of understanding this lifecycle, you only need to know that Angular walks your application tree from top to bottom, checking template bindings for changes. The lifecycle hooks described below run while Angular is doing this traversal. This traversal visits each component exactly once, so you should always avoid making further state changes in the middle of the process.

## Summary

|  |  |  |
| --- | --- | --- |
| **Phase** | **Method** | **Summary** |
| Creation | `constructor` | [Standard JavaScript class constructor](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Classes/constructor) . Runs when Angular instantiates the component. |
| Change Detection | `ngOnInit` | Runs once after Angular has initialized all the component's inputs. |
| `ngOnChanges` | Runs every time the component's inputs have changed. |
| `ngDoCheck` | Runs every time this component is checked for changes. |
| `ngAfterContentInit` | Runs once after the component's *content* has been initialized. |
| `ngAfterContentChecked` | Runs every time this component content has been checked for changes. |
| `ngAfterViewInit` | Runs once after the component's *view* has been initialized. |
| `ngAfterViewChecked` | Runs every time the component's view has been checked for changes. |
| Rendering | `afterNextRender` | Runs once the next time that **all** components have been rendered to the DOM. |
| `afterEveryRender` | Runs every time **all** components have been rendered to the DOM. |
| Destruction | `ngOnDestroy` | Runs once before the component is destroyed. |

### ngOnInit

The `ngOnInit` method runs after Angular has initialized all the components inputs with their initial values. A component's `ngOnInit` runs exactly once.

This step happens *before* the component's own template is initialized. This means that you can update the component's state based on its initial input values.

### ngOnChanges

The `ngOnChanges` method runs after any component inputs have changed.

This step happens *before* the component's own template is checked. This means that you can update the component's state based on its initial input values.

During initialization, the first `ngOnChanges` runs before `ngOnInit`.

#### Inspecting changes

The `ngOnChanges` method accepts one [`SimpleChanges`](../../api/core/simplechanges) argument. This object is a [`Record`](https://www.typescriptlang.org/docs/handbook/utility-types.html#recordkeys-type) mapping each component input name to a [`SimpleChange`](../../api/core/simplechange) object. Each [`SimpleChange`](../../api/core/simplechange) contains the input's previous value, its current value, and a flag for whether this is the first time the input has changed.

You can optionally pass the current class or this as the first generic argument for stronger type checking.

```
@Component({
  /* ... */
})
export class UserProfile {
  name = input('');

  ngOnChanges(changes: SimpleChanges<UserProfile>) {
    if (changes.name) {
      console.log(`Previous: ${changes.name.previousValue}`);
      console.log(`Current: ${changes.name.currentValue}`);
      console.log(`Is first ${changes.name.firstChange}`);
    }
  }
}
```

If you provide an `alias` for any input properties, the [`SimpleChanges`](../../api/core/simplechanges) Record still uses the TypeScript property name as a key, rather than the alias.

### ngOnDestroy

The `ngOnDestroy` method runs once just before a component is destroyed. Angular destroys a component when it is no longer shown on the page, such as being hidden by `@if` or upon navigating to another page.

#### DestroyRef

As an alternative to the `ngOnDestroy` method, you can inject an instance of [`DestroyRef`](../../api/core/destroyref). You can register a callback to be invoked upon the component's destruction by calling the `onDestroy` method of [`DestroyRef`](../../api/core/destroyref).

```
@Component({
  /* ... */
})
export class UserProfile {
  constructor() {
    inject(DestroyRef).onDestroy(() => {
      console.log('UserProfile destruction');
    });
  }
}
```

You can pass the [`DestroyRef`](../../api/core/destroyref) instance to functions or classes outside your component. Use this pattern if you have other code that should run some cleanup behavior when the component is destroyed.

You can also use [`DestroyRef`](../../api/core/destroyref) to keep setup code close to cleanup code, rather than putting all cleanup code in the `ngOnDestroy` method.

##### [Detecting instance destruction](#detecting-instance-destruction)

[`DestroyRef`](../../api/core/destroyref) provides a `destroyed` property that allows checking whether a given instance has already been destroyed. This is useful for avoiding operations on destroyed components, especially when dealing with delayed or asynchronous logic.

By checking `destroyRef.destroyed`, you can prevent executing code after the instance has been cleaned up, avoiding potential errors such as `NG0911: View has already been destroyed.`.

### ngDoCheck

The `ngDoCheck` method runs before every time Angular checks a component's template for changes.

You can use this lifecycle hook to manually check for state changes outside of Angular's normal change detection, manually updating the component's state.

This method runs very frequently and can significantly impact your page's performance. Avoid defining this hook whenever possible, only using it when you have no alternative.

During initialization, the first `ngDoCheck` runs after `ngOnInit`.

### ngAfterContentInit

The `ngAfterContentInit` method runs once after all the children nested inside the component (its *content*) have been initialized.

You can use this lifecycle hook to read the results of [content queries](queries#content-queries). While you can access the initialized state of these queries, attempting to change any state in this method results in an [ExpressionChangedAfterItHasBeenCheckedError](https://angular.dev/errors/NG0100)

### ngAfterContentChecked

The `ngAfterContentChecked` method runs every time the children nested inside the component (its *content*) have been checked for changes.

This method runs very frequently and can significantly impact your page's performance. Avoid defining this hook whenever possible, only using it when you have no alternative.

While you can access the updated state of [content queries](queries#content-queries) here, attempting to change any state in this method results in an [ExpressionChangedAfterItHasBeenCheckedError](https://angular.dev/errors/NG0100).

### ngAfterViewInit

The `ngAfterViewInit` method runs once after all the children in the component's template (its *view*) have been initialized.

You can use this lifecycle hook to read the results of [view queries](queries#view-queries). While you can access the initialized state of these queries, attempting to change any state in this method results in an [ExpressionChangedAfterItHasBeenCheckedError](https://angular.dev/errors/NG0100)

### ngAfterViewChecked

The `ngAfterViewChecked` method runs every time the children in the component's template (its *view*) have been checked for changes.

This method runs very frequently and can significantly impact your page's performance. Avoid defining this hook whenever possible, only using it when you have no alternative.

While you can access the updated state of [view queries](queries#view-queries) here, attempting to change any state in this method results in an [ExpressionChangedAfterItHasBeenCheckedError](https://angular.dev/errors/NG0100).

### afterEveryRender and afterNextRender

The [`afterEveryRender`](../../api/core/aftereveryrender) and [`afterNextRender`](../../api/core/afternextrender) functions let you register a **render callback** to be invoked after Angular has finished rendering *all components* on the page into the DOM.

These functions are different from the other lifecycle hooks described in this guide. Rather than a class method, they are standalone functions that accept a callback. The execution of render callbacks are not tied to any specific component instance, but instead an application-wide hook.

[`afterEveryRender`](../../api/core/aftereveryrender) and [`afterNextRender`](../../api/core/afternextrender) must be called in an [injection context](../di/dependency-injection-context), typically a component's constructor.

You can use render callbacks to perform manual DOM operations. See [Using DOM APIs](dom-apis) for guidance on working with the DOM in Angular.

Render callbacks do not run during server-side rendering or during build-time pre-rendering.

#### after\*Render phases

When using [`afterEveryRender`](../../api/core/aftereveryrender) or [`afterNextRender`](../../api/core/afternextrender), you can optionally split the work into phases. The phase gives you control over the sequencing of DOM operations, letting you sequence *write* operations before *read* operations in order to minimize [layout thrashing](https://web.dev/avoid-large-complex-layouts-and-layout-thrashing). In order to communicate across phases, a phase function may return a result value that can be accessed in the next phase.

```
import {Component, ElementRef, afterNextRender} from '@angular/core';

@Component({...})
export class UserProfile {
  private prevPadding = 0;
  private elementHeight = 0;

  constructor() {
    private elementRef = inject(ElementRef);
    const nativeElement = elementRef.nativeElement;

    afterNextRender({
      // Use the `Write` phase to write to a geometric property.
      write: () => {
        const padding = computePadding();
        const changed = padding !== this.prevPadding;
        if (changed) {
          nativeElement.style.padding = padding;
        }
        return changed; // Communicate whether anything changed to the read phase.
      },

      // Use the `Read` phase to read geometric properties after all writes have occurred.
      read: (didWrite) => {
        if (didWrite) {
          this.elementHeight = nativeElement.getBoundingClientRect().height;
        }
      }
    });
  }
}
```

There are four phases, run in the following order:

| Phase | Description |
| --- | --- |
| `earlyRead` | Use this phase to read any layout-affecting DOM properties and styles that are strictly necessary for subsequent calculation. Avoid this phase if possible, preferring the `write` and `read` phases. |
| `write` | Use this phase to write layout-affecting DOM properties and styles. |
| `mixedReadWrite` | Default phase. Use for any operations need to both read and write layout-affecting properties and styles. Avoid this phase if possible, preferring the explicit `write` and `read` phases. |
| `read` | Use this phase to read any layout-affecting DOM properties. |

## Lifecycle interfaces

Angular provides a TypeScript interface for each lifecycle method. You can optionally import and `implement` these interfaces to ensure that your implementation does not have any typos or misspellings.

Each interface has the same name as the corresponding method without the `ng` prefix. For example, the interface for `ngOnInit` is [`OnInit`](../../api/core/oninit).

```
@Component({
  /* ... */
})
export class UserProfile implements OnInit {
  ngOnInit() {
    /* ... */
  }
}
```

## Execution order

The following diagrams show the execution order of Angular's lifecycle hooks.

### During initialization

Rendering

Change detection

ngOnChanges

ngOnInit

ngDoCheck

ngAfterContentInit

ngAfterViewInit

ngAfterContentChecked

ngAfterViewChecked

constructor

afterNextRender

afterEveryRender

### Subsequent updates

Rendering

Change detection

ngOnChanges

ngDoCheck

ngAfterContentChecked

ngAfterViewChecked

afterEveryRender

### Ordering with directives

When you put one or more directives on the same element as a component, either in a template or with the `hostDirectives` property, the framework does not guarantee any ordering of a given lifecycle hook between the component and the directives on a single element. Never depend on an observed ordering, as this may change in later versions of Angular.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/guide/components/lifecycle>
