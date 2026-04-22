# Component host elements

Component host elements



# Component host elements

  

**TIP:** This guide assumes you've already read the [Essentials Guide](https://angular.dev/essentials). Read that first if you're new to Angular.

Angular creates an instance of a component for every HTML element that matches the component's selector. The DOM element that matches a component's selector is that component's **host element**. The contents of a component's template are rendered inside its host element.

```
// Component source
@Component({
  selector: 'profile-photo',
  template: `
    <img src="profile-photo.jpg" alt="Your profile photo" />
  `,
})
export class ProfilePhoto {}
```

```
<!-- Using the component -->
<h3>Your profile photo</h3>
<profile-photo />
<button>Upload a new profile photo</button>
```

```
<!-- Rendered DOM -->
<h3>Your profile photo</h3>
<profile-photo>
  <img src="profile-photo.jpg" alt="Your profile photo" />
</profile-photo>
<button>Upload a new profile photo</button>
```

In the above example, `<profile-photo>` is the host element of the `ProfilePhoto` component.

## Binding to the host element

A component can bind properties, attributes, styles and events to its host element. This behaves identically to bindings on elements inside the component's template, but instead defined with the `host` property in the [`@Component`](../../api/core/component) decorator:

```
@Component({
  ...,
  host: {
    'role': 'slider',
    '[attr.aria-valuenow]': 'value',
    '[class.active]': 'isActive()',
    '[style.background]' : `hasError() ? 'red' : 'green'`,
    '[tabIndex]': 'disabled ? -1 : 0',
    '(keydown)': 'updateValue($event)',
  },
})
export class CustomSlider {
  value: number = 0;
  disabled: boolean = false;
  isActive = signal(false);
  hasError = signal(false);
  updateValue(event: KeyboardEvent) { /* ... */ }

  /* ... */
}
```

## The @HostBinding and @HostListener decorators

You can alternatively bind to the host element by applying the [`@HostBinding`](../../api/core/hostbinding) and [`@HostListener`](../../api/core/hostlistener) decorator to class members.

[`@HostBinding`](../../api/core/hostbinding) lets you bind host properties and attributes to properties and getters:

```
@Component({
  /* ... */
})
export class CustomSlider {
  @HostBinding('attr.aria-valuenow')
  value: number = 0;

  @HostBinding('tabIndex')
  get tabIndex() {
    return this.disabled ? -1 : 0;
  }

  /* ... */
}
```

[`@HostListener`](../../api/core/hostlistener) lets you bind event listeners to the host element. The decorator accepts an event name and an optional array of arguments:

```
export class CustomSlider {
  @HostListener('keydown', ['$event'])
  updateValue(event: KeyboardEvent) {
    /* ... */
  }
}
```

### Prefer using the host property over the decorators

**Always prefer using the `host` property over [`@HostBinding`](../../api/core/hostbinding) and [`@HostListener`](../../api/core/hostlistener).** These decorators exist exclusively for backwards compatibility.

## Binding collisions

When you use a component in a template, you can add bindings to that component instance's element. The component may *also* define host bindings for the same properties or attributes.

```
@Component({
  ...,
  host: {
    'role': 'presentation',
    '[id]': 'id',
  }
})
export class ProfilePhoto { /* ... */ }
```

```
<profile-photo role="group" [id]="otherId" />
```

In cases like this, the following rules determine which value wins:

- If both values are static, the instance binding wins.
- If one value is static and the other dynamic, the dynamic value wins.
- If both values are dynamic, the component's host binding wins.

## Styling with CSS custom properties

Developers often rely on [CSS Custom Properties](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_cascading_variables/Using_CSS_custom_properties) to enable a flexible configuration of their component's styles. You can set such custom properties on a host element with a [style binding][style binding](../templates/binding#css-style-properties).

```
@Component({
  /* ... */
  host: {
    '[style.--my-background]': 'color()',
  }
})
export class MyComponent {
  color = signal('lightgreen');
}
```

In this example, the `--my-background` CSS custom property is bound to the `color` signal. The value of the custom property will automatically update whenever the `color` signal changes. This will affect the current component and all its children that rely on this custom property.

### Setting custom properties on children compoents

Alternatively, it is also possible to set css custom properties on the host element of children components with a [style binding](../templates/binding#css-style-properties).

```
@Component({
  selector: 'my-component',
  template: `<my-child [style.--my-background]="color()">`,
})
export class MyComponent {
  color = signal('lightgreen');
}
```

## Injecting host element attributes

Components and directives can read static attributes from their host element by using [`HostAttributeToken`](../../api/core/hostattributetoken) together with the [`inject`](../../api/core/inject) function.

```
import { Component, HostAttributeToken, inject } from '@angular/core';

@Component({
  selector: 'app-button',
  ...,
})
export class Button {
  variation = inject(new HostAttributeToken('variation'));
}
```

```
<app-button variation="primary">Click me</app-button>
```

**HELPFUL:** [`HostAttributeToken`](../../api/core/hostattributetoken) throws an error if the attribute is missing, unless the injection is marked as optional.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/guide/components/host-elements>
