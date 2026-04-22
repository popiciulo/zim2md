# style

style



# style

Declares a key/value object containing CSS properties/styles that can then be used for an animation [`state`](state), within an animation [`sequence`](sequence), or as styling data for calls to [`animate()`](animate) and [`keyframes()`](keyframes).

Deprecation warning

Use `animate.enter` or `animate.leave` instead. Intent to remove in v23

## API

```
function style(
  tokens:
    | '*'
    | { [key: string]: string | number }
    | ('*' | { [key: string]: string | number })[],
): AnimationStyleMetadata;
```

### style

`AnimationStyleMetadata`

Declares a key/value object containing CSS properties/styles that can then be used for an animation [`state`](state), within an animation [`sequence`](sequence), or as styling data for calls to [`animate()`](animate) and [`keyframes()`](keyframes).

@deprecated

Use `animate.enter` or `animate.leave` instead. Intent to remove in v23

@paramtokens`"*" | { [key: string]: string | number; } | ("*" | { [key: string]: string | number; })[]`

A set of CSS styles or HTML styles associated with an animation state. The value can be any of the following:

- A key-value style pair associating a CSS property with a value.
- An array of key-value style pairs.
- An asterisk (\*), to use auto-styling, where styles are derived from the element being animated and applied to the animation when it starts.

Auto-styling can be used to define a state that depends on layout or other environmental factors.

@returns`AnimationStyleMetadata`

Usage notes

The following examples create animation styles that collect a set of CSS property values:

```
// string values for CSS properties
style({ background: "red", color: "blue" })

// numerical pixel values
style({ width: 100, height: 0 })
```

The following example uses auto-styling to allow an element to animate from a height of 0 up to its full height:

```
style({ height: 0 }),
animate("1s", style({ height: "*" }))
```

## Usage Notes

The following examples create animation styles that collect a set of CSS property values:

```
// string values for CSS properties
style({ background: "red", color: "blue" })

// numerical pixel values
style({ width: 100, height: 0 })
```

The following example uses auto-styling to allow an element to animate from a height of 0 up to its full height:

```
style({ height: 0 }),
animate("1s", style({ height: "*" }))
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/animations/style>
