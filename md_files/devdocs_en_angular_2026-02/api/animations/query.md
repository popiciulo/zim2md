# query

query



# query

Finds one or more inner elements within the current element that is being animated within a sequence. Use with [`animate()`](animate).

Deprecation warning

Use `animate.enter` or `animate.leave` instead. Intent to remove in v23

## API

```
function query(
  selector: string,
  animation: AnimationMetadata | AnimationMetadata[],
  options?: AnimationQueryOptions | null,
): AnimationQueryMetadata;
```

### query

`AnimationQueryMetadata`

Finds one or more inner elements within the current element that is being animated within a sequence. Use with [`animate()`](animate).

@deprecated

Use `animate.enter` or `animate.leave` instead. Intent to remove in v23

@paramselector`string`

The element to query, or a set of elements that contain Angular-specific characteristics, specified with one or more of the following tokens.

- `query(":enter")` or `query(":leave")` : Query for newly inserted/removed elements (not all elements can be queried via these tokens, see [Entering and Leaving Elements](#entering-and-leaving-elements))
- `query(":animating")` : Query all currently animating elements.
- `query("@triggerName")` : Query elements that contain an animation trigger.
- `query("@*")` : Query all elements that contain an animation triggers.
- `query(":self")` : Include the current element into the animation sequence.

@paramanimation`AnimationMetadata | AnimationMetadata[]`

One or more animation steps to apply to the queried element or elements. An array is treated as an animation sequence.

@paramoptions`AnimationQueryOptions | null`

An options object. Use the 'limit' field to limit the total number of items to collect.

@returns`AnimationQueryMetadata`

Usage notes

### Multiple Tokens

Tokens can be merged into a combined query selector string. For example:

```
 query(':self, .record:enter, .record:leave,
```

## Usage Notes

### Multiple Tokens

Tokens can be merged into a combined query selector string. For example:

```
 query(':self, .record:enter, .record:leave,
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/animations/query>
