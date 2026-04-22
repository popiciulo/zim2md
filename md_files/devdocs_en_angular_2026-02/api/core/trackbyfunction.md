# TrackByFunction

TrackByFunction



# TrackByFunction

A function optionally passed into the `NgForOf` directive to customize how `NgForOf` uniquely identifies items in an iterable.

[`NgForOf#ngForTrackBy`](../common/ngforof#ngForTrackBy)

## API

```
interface TrackByFunction<T> {
  <U extends T>(index: number, item: T & U): any;
}
```

`any`

@paramindex`number`

The index of the item within the iterable.

@paramitem`T & U`

The item in the iterable.

@returns`any`

## Description

A function optionally passed into the `NgForOf` directive to customize how `NgForOf` uniquely identifies items in an iterable.

`NgForOf` needs to uniquely identify items in the iterable to correctly perform DOM updates when items in the iterable are reordered, new items are added, or existing items are removed.

In all of these scenarios it is usually desirable to only update the DOM elements associated with the items affected by the change. This behavior is important to:

- preserve any DOM-specific UI state (like cursor position, focus, text selection) when the iterable is modified
- enable animation of item addition, removal, and iterable reordering
- preserve the value of the `<select>` element when nested `<option>` elements are dynamically populated using `NgForOf` and the bound iterable is updated

A common use for custom `trackBy` functions is when the model that `NgForOf` iterates over contains a property with a unique identifier. For example, given a model:

```
class User {
  id: number;
  name: string;
  ...
}
```

a custom `trackBy` function could look like the following:

```
function userTrackBy(index, user) {
  return user.id;
}
```

A custom `trackBy` function must have several properties:

- be [idempotent](https://en.wikipedia.org/wiki/Idempotence) (be without side effects, and always return the same value for a given input)
- return unique value for all unique inputs
- be fast

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/TrackByFunction>
