# NgForOf

NgForOf



# NgForOf

A [structural directive](../../guide/directives/structural-directives) that renders a template for each item in a collection. The directive is placed on an element, which becomes the parent of the cloned templates.

[Structural Directives](../../guide/directives/structural-directives)

Deprecation warning

Use the `@for` block instead. Intent to remove in v22

## API

```
class NgForOf<T, U extends NgIterable<T> = NgIterable<T>> implements DoCheck {
  constructor(_viewContainer: ViewContainerRef, _template: TemplateRef<NgForOfContext<T, U>>, _differs: IterableDiffers): NgForOf<T, U>;
  @Input() set ngForOf(value: (U & NgIterable<T>) | null | undefined);
  @Input() get ngForTrackBy(): TrackByFunction<T>;
  @Input() set ngForTemplate(value: TemplateRef<NgForOfContext<T, U>>);
  static ngTemplateContextGuard<T, U extends NgIterable<T>>(dir: NgForOf<T, U>, ctx: any): ctx is NgForOfContext<T, U>;
}
```

### constructor

`NgForOf<T, U>`

@param\_viewContainer`ViewContainerRef`

@param\_template`TemplateRef<NgForOfContext<T, U>>`

@param\_differs`IterableDiffers`

@returns`NgForOf<T, U>`

### ngForOf

`(U & NgIterable<T>) | null | undefined`

@deprecated

The `ngFor` directive is deprecated. Use the `@for` block instead.

The value of the iterable expression, which can be used as a [template input variable](../../guide/directives/structural-directives#shorthand).

### ngForTrackBy

`TrackByFunction<T>`

@deprecated

The `ngFor` directive is deprecated. Use the `@for` block instead.

Specifies a custom [`TrackByFunction`](../core/trackbyfunction) to compute the identity of items in an iterable.

If a custom [`TrackByFunction`](../core/trackbyfunction) is not provided, [`NgForOf`](ngforof) will use the item's [object identity](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/is) as the key.

[`NgForOf`](ngforof) uses the computed key to associate items in an iterable with DOM elements it produces for these items.

A custom [`TrackByFunction`](../core/trackbyfunction) is useful to provide good user experience in cases when items in an iterable rendered using [`NgForOf`](ngforof) have a natural identifier (for example, custom ID or a primary key), and this iterable could be updated with new object instances that still represent the same underlying entity (for example, when data is re-fetched from the server, and the iterable is recreated and re-rendered, but most of the data is still the same).

### ngForTrackBy

`TrackByFunction<T>`

### ngForTemplate

`TemplateRef<NgForOfContext<T, U>>`

@deprecated

The `ngFor` directive is deprecated. Use the `@for` block instead.

A reference to the template that is stamped out for each item in the iterable.

### ngTemplateContextGuard

`ctx is NgForOfContext<T, U>`

Asserts the correct type of the context for the template that [`NgForOf`](ngforof) will render.

The presence of this method is a signal to the Ivy template type-check compiler that the [`NgForOf`](ngforof) structural directive renders its template with a specific context type.

@paramdir`NgForOf<T, U>`

@paramctx`any`

@returns`ctx is NgForOfContext<T, U>`

## Description

A [structural directive](../../guide/directives/structural-directives) that renders a template for each item in a collection. The directive is placed on an element, which becomes the parent of the cloned templates.

The `ngForOf` directive is generally used in the [shorthand form](../../guide/directives/structural-directives#asterisk) `*ngFor`. In this form, the template to be rendered for each iteration is the content of an anchor element containing the directive.

The following example shows the shorthand syntax with some options, contained in an `<li>` element.

```
<li *ngFor="let item of items; index as i; trackBy: trackByFn">...</li>
```

The shorthand form expands into a long form that uses the `ngForOf` selector on an `<ng-template>` element. The content of the `<ng-template>` element is the `<li>` element that held the short-form directive.

Here is the expanded version of the short-form example.

```
<ng-template ngFor let-item [ngForOf]="items" let-i="index" [ngForTrackBy]="trackByFn">
  <li>...</li>
</ng-template>
```

Angular automatically expands the shorthand syntax as it compiles the template. The context for each embedded view is logically merged to the current component context according to its lexical position.

When using the shorthand syntax, Angular allows only [one structural directive on an element](../../guide/directives/structural-directives#one-per-element). If you want to iterate conditionally, for example, put the `*ngIf` on a container element that wraps the `*ngFor` element. For further discussion, see [Structural Directives](../../guide/directives/structural-directives#one-per-element).

---

## Exported by

- `CommonModule`

## Usage Notes

### Local variables

[`NgForOf`](ngforof) provides exported values that can be aliased to local variables. For example:

```
<li *ngFor="let user of users; index as i; first as isFirst">
   {{i}}/{{users.length}}. {{user}} <span *ngIf="isFirst">default</span>
</li>
```

The following exported values can be aliased to local variables:

- `$implicit: T`: The value of the individual items in the iterable (`ngForOf`).
- `ngForOf: NgIterable<T>`: The value of the iterable expression. Useful when the expression is more complex then a property access, for example when using the async pipe (`userStreams | async`).
- `index: number`: The index of the current item in the iterable.
- `count: number`: The length of the iterable.
- `first: boolean`: True when the item is the first item in the iterable.
- `last: boolean`: True when the item is the last item in the iterable.
- `even: boolean`: True when the item has an even index in the iterable.
- `odd: boolean`: True when the item has an odd index in the iterable.

### Change propagation

When the contents of the iterator changes, [`NgForOf`](ngforof) makes the corresponding changes to the DOM:

- When an item is added, a new instance of the template is added to the DOM.
- When an item is removed, its template instance is removed from the DOM.
- When items are reordered, their respective templates are reordered in the DOM.

Angular uses object identity to track insertions and deletions within the iterator and reproduce those changes in the DOM. This has important implications for animations and any stateful controls that are present, such as `<input>` elements that accept user input. Inserted rows can be animated in, deleted rows can be animated out, and unchanged rows retain any unsaved state such as user input. For more on animations, see [Transitions and Triggers](../../guide/animations/transition-and-triggers).

The identities of elements in the iterator can change while the data does not. This can happen, for example, if the iterator is produced from an RPC to the server, and that RPC is re-run. Even if the data hasn't changed, the second response produces objects with different identities, and Angular must tear down the entire DOM and rebuild it (as if all old elements were deleted and all new elements inserted).

To avoid this expensive operation, you can customize the default tracking algorithm. by supplying the `trackBy` option to [`NgForOf`](ngforof). `trackBy` takes a function that has two arguments: `index` and `item`. If `trackBy` is given, Angular tracks changes by the return value of the function.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/NgForOf>
