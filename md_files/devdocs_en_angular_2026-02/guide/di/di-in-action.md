# DI in action

DI in action



# DI in action

  

This guide explores additional features of dependency injection in Angular.

**NOTE:** For comprehensive coverage of InjectionToken and custom providers, see the [defining dependency providers guide](defining-dependency-providers#injection-tokens).

## Inject the component's DOM element

Although developers strive to avoid it, some visual effects and third-party tools require direct DOM access. As a result, you might need to access a component's DOM element.

Angular exposes the underlying element of a [`@Component`](../../api/core/component) or [`@Directive`](../../api/core/directive) via injection using the [`ElementRef`](../../api/core/elementref) injection token:

```
import {Directive, ElementRef, inject} from '@angular/core';

@Directive({
  selector: '[appHighlight]',
})
export class HighlightDirective {
  private element = inject(ElementRef);

  update() {
    this.element.nativeElement.style.color = 'red';
  }
}
```

## Resolve circular dependencies with a forward reference

The order of class declaration matters in TypeScript. You can't refer directly to a class until it's been defined.

This isn't usually a problem, especially if you adhere to the recommended *one class per file* rule. But sometimes circular references are unavoidable. For example, when class 'A' refers to class 'B' and 'B' refers to 'A', one of them has to be defined first.

The Angular [`forwardRef()`](../../api/core/forwardref) function creates an *indirect* reference that Angular can resolve later.

You face a similar problem when a class makes *a reference to itself*. For example, in its `providers` array. The `providers` array is a property of the [`@Component()`](../../api/core/component) decorator function, which must appear before the class definition. You can break such circular references by using [`forwardRef`](../../api/core/forwardref).

```
providers: [
  {
    provide: PARENT_MENU_ITEM,
    useExisting: forwardRef(() => MenuItem),
  },
],
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/guide/di/di-in-action>
