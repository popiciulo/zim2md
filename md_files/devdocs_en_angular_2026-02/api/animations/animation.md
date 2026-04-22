# animation

animation



# animation

Produces a reusable animation that can be invoked in another animation or sequence, by calling the [`useAnimation()`](useanimation) function.

Deprecation warning

Use `animate.enter` or `animate.leave` instead. Intent to remove in v23

## API

```
function animation(
  steps: AnimationMetadata | AnimationMetadata[],
  options?: AnimationOptions | null,
): AnimationReferenceMetadata;
```

### animation

`AnimationReferenceMetadata`

Produces a reusable animation that can be invoked in another animation or sequence, by calling the [`useAnimation()`](useanimation) function.

@deprecated

Use `animate.enter` or `animate.leave` instead. Intent to remove in v23

@paramsteps`AnimationMetadata | AnimationMetadata[]`

One or more animation objects, as returned by the [`animate()`](animate) or [`sequence()`](sequence) function, that form a transformation from one state to another. A sequence is used by default when you pass an array.

@paramoptions`AnimationOptions | null`

An options object that can contain a delay value for the start of the animation, and additional developer-defined parameters. Provided values for additional parameters are used as defaults, and override values can be passed to the caller on invocation.

@returns`AnimationReferenceMetadata`

Usage notes

The following example defines a reusable animation, providing some default parameter values.

```
var fadeAnimation = animation([
  style({ opacity: '{{ start }}' }),
  animate('{{ time }}',
  style({ opacity: '{{ end }}'}))
  ],
  { params: { time: '1000ms', start: 0, end: 1 }});
```

The following invokes the defined animation with a call to [`useAnimation()`](useanimation), passing in override parameter values.

```
useAnimation(fadeAnimation, {
  params: {
    time: '2s',
    start: 1,
    end: 0
  }
})
```

If any of the passed-in parameter values are missing from this call, the default values are used. If one or more parameter values are missing before a step is animated, [`useAnimation()`](useanimation) throws an error.

## Usage Notes

The following example defines a reusable animation, providing some default parameter values.

```
var fadeAnimation = animation([
  style({ opacity: '{{ start }}' }),
  animate('{{ time }}',
  style({ opacity: '{{ end }}'}))
  ],
  { params: { time: '1000ms', start: 0, end: 1 }});
```

The following invokes the defined animation with a call to [`useAnimation()`](useanimation), passing in override parameter values.

```
useAnimation(fadeAnimation, {
  params: {
    time: '2s',
    start: 1,
    end: 0
  }
})
```

If any of the passed-in parameter values are missing from this call, the default values are used. If one or more parameter values are missing before a step is animated, [`useAnimation()`](useanimation) throws an error.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/animations/animation>
