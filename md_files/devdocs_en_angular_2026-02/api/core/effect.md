# effect

effect



# effect

Registers an "effect" that will be scheduled & executed whenever the signals that it reads changes.

[Effects](../../guide/signals#effects)

## API

```
function effect(
  effectFn: (onCleanup: EffectCleanupRegisterFn) => void,
  options?: CreateEffectOptions | undefined,
): EffectRef;
```

### effect

`EffectRef`

Registers an "effect" that will be scheduled & executed whenever the signals that it reads changes.

Angular has two different kinds of effect: component effects and root effects. Component effects are created when [`effect()`](effect) is called from a component, directive, or within a service of a component/directive. Root effects are created when [`effect()`](effect) is called from outside the component tree, such as in a root service.

The two effect types differ in their timing. Component effects run as a component lifecycle event during Angular's synchronization (change detection) process, and can safely read input signals or create/destroy views that depend on component state. Root effects run as microtasks and have no connection to the component tree or change detection.

[`effect()`](effect) must be run in injection context, unless the `injector` option is manually specified.

@parameffectFn`(onCleanup: EffectCleanupRegisterFn) => void`

@paramoptions`CreateEffectOptions | undefined`

@returns`EffectRef`

## Description

Registers an "effect" that will be scheduled & executed whenever the signals that it reads changes.

Angular has two different kinds of effect: component effects and root effects. Component effects are created when [`effect()`](effect) is called from a component, directive, or within a service of a component/directive. Root effects are created when [`effect()`](effect) is called from outside the component tree, such as in a root service.

The two effect types differ in their timing. Component effects run as a component lifecycle event during Angular's synchronization (change detection) process, and can safely read input signals or create/destroy views that depend on component state. Root effects run as microtasks and have no connection to the component tree or change detection.

[`effect()`](effect) must be run in injection context, unless the `injector` option is manually specified.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/effect>
