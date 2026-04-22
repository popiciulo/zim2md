# EmbeddedViewRef

EmbeddedViewRef



# EmbeddedViewRef

Represents an Angular view in a view container. An embedded view can be referenced from a component other than the hosting component whose template defines it, or it can be defined independently by a [`TemplateRef`](templateref).

[ViewContainerRef](viewcontainerref)

## API

```
abstract class EmbeddedViewRef<C> extends ViewRef {
  abstract context: C;
  abstract readonly rootNodes: any[];
  abstract override destroy(): void;
  abstract override readonly destroyed: boolean;
  abstract override onDestroy(callback: Function): void;
  abstract override markForCheck(): void;
  abstract override detach(): void;
  abstract override detectChanges(): void;
  abstract override checkNoChanges(): void;
  abstract override reattach(): void;
}
```

### context

`C`

The context for this view, inherited from the anchor element.

### rootNodes

`any[]`

The root nodes for this embedded view.

### destroy

`void`

Destroys this view and all of the data structures associated with it.

@returns`void`

### destroyed

`boolean`

Reports whether this view has been destroyed.

### onDestroy

`void`

A lifecycle hook that provides additional developer-defined cleanup functionality for views.

@paramcallback`Function`

A handler function that cleans up developer-defined data associated with a view. Called when the `destroy()` method is invoked.

@returns`void`

### markForCheck

`void`

When a view uses the [`ChangeDetectionStrategy#OnPush`](changedetectionstrategy#OnPush) (checkOnce) change detection strategy, explicitly marks the view as changed so that it can be checked again.

Components are normally marked as dirty (in need of rerendering) when inputs have changed or events have fired in the view. Call this method to ensure that a component is checked even if these triggers have not occurred.

@returns`void`

### detach

`void`

Detaches this view from the change-detection tree. A detached view is not checked until it is reattached. Use in combination with `detectChanges()` to implement local change detection checks.

Detached views are not checked during change detection runs until they are re-attached, even if they are marked as dirty.

@returns`void`

### detectChanges

`void`

Checks this view and its children. Use in combination with [`ChangeDetectorRef#detach`](changedetectorref#detach) to implement local change detection checks.

@returns`void`

### checkNoChanges

`void`

Checks the change detector and its children, and throws if any changes are detected.

Use in development mode to verify that running change detection doesn't introduce other changes. Calling it in production mode is a noop.

@deprecated

This is a test-only API that does not have a place in production interface. `checkNoChanges` is already part of an [`ApplicationRef`](applicationref) tick when the app is running in dev mode. For more granular `checkNoChanges` validation, use `ComponentFixture`.

@returns`void`

### reattach

`void`

Re-attaches the previously detached view to the change detection tree. Views are attached to the tree by default.

@returns`void`

## Description

Represents an Angular view in a view container. An embedded view can be referenced from a component other than the hosting component whose template defines it, or it can be defined independently by a [`TemplateRef`](templateref).

Properties of elements in a view can change, but the structure (number and order) of elements in a view cannot. Change the structure of elements by inserting, moving, or removing nested views in a view container.

## Usage Notes

The following template breaks down into two separate [`TemplateRef`](templateref) instances, an outer one and an inner one.

```
Count: {{items.length}}
<ul>
  <li *ngFor="let  item of items">{{item}}</li>
</ul>
```

This is the outer [`TemplateRef`](templateref):

```
Count: {{items.length}}
<ul>
  <ng-template ngFor let-item [ngForOf]="items"></ng-template>
</ul>
```

This is the inner [`TemplateRef`](templateref):

```
  <li>{{item}}</li>
```

The outer and inner [`TemplateRef`](templateref) instances are assembled into views as follows:

```
<!-- ViewRef: outer-0 -->
Count: 2
<ul>
  <ng-template view-container-ref></ng-template>
  <!-- ViewRef: inner-1 --><li>first</li><!-- /ViewRef: inner-1 -->
  <!-- ViewRef: inner-2 --><li>second</li><!-- /ViewRef: inner-2 -->
</ul>
<!-- /ViewRef: outer-0 -->
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/EmbeddedViewRef>
