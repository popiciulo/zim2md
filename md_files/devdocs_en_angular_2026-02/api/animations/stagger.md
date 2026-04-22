# stagger

stagger



# stagger

Use within an animation [`query()`](query) call to issue a timing gap after each queried item is animated.

Deprecation warning

Use `animate.enter` or `animate.leave` instead. Intent to remove in v23

## API

```
function stagger(
  timings: string | number,
  animation: AnimationMetadata | AnimationMetadata[],
): AnimationStaggerMetadata;
```

### stagger

`AnimationStaggerMetadata`

Use within an animation [`query()`](query) call to issue a timing gap after each queried item is animated.

@deprecated

Use `animate.enter` or `animate.leave` instead. Intent to remove in v23

@paramtimings`string | number`

A delay value.

@paramanimation`AnimationMetadata | AnimationMetadata[]`

One ore more animation steps.

@returns`AnimationStaggerMetadata`

Usage notes

In the following example, a container element wraps a list of items stamped out by an `@for` block. The container element contains an animation trigger that will later be set to query for each of the inner items.

Each time items are added, the opacity fade-in animation runs, and each removed item is faded out. When either of these animations occur, the stagger effect is applied after each item's animation is started.

```
<!-- list.component.html -->
<button (click)="toggle()">Show / Hide Items</button>
<hr />
<div [@listAnimation]="items.length">
  @for(item of items; track $index) {
     <div>{{ item }}</div>
  }
</div>
```

Here is the component code:

```
import {trigger, transition, style, animate, query, stagger} from '@angular/animations';
@Component({
  templateUrl: 'list.component.html',
  animations: [
    trigger('listAnimation', [
    ...
    ])
  ]
})
class ListComponent {
  items = [];

  showItems() {
    this.items = [0,1,2,3,4];
  }

  hideItems() {
    this.items = [];
  }

  toggle() {
    this.items.length ? this.hideItems() : this.showItems();
   }
 }
```

Here is the animation trigger code:

```
trigger('listAnimation', [
  transition('* => *', [ // each time the binding value changes
    query(':leave', [
      stagger(100, [
        animate('0.5s', style({ opacity: 0 }))
      ])
    ]),
    query(':enter', [
      style({ opacity: 0 }),
      stagger(100, [
        animate('0.5s', style({ opacity: 1 }))
      ])
    ])
  ])
])
```

## Usage Notes

In the following example, a container element wraps a list of items stamped out by an `@for` block. The container element contains an animation trigger that will later be set to query for each of the inner items.

Each time items are added, the opacity fade-in animation runs, and each removed item is faded out. When either of these animations occur, the stagger effect is applied after each item's animation is started.

```
<!-- list.component.html -->
<button (click)="toggle()">Show / Hide Items</button>
<hr />
<div [@listAnimation]="items.length">
  @for(item of items; track $index) {
     <div>{{ item }}</div>
  }
</div>
```

Here is the component code:

```
import {trigger, transition, style, animate, query, stagger} from '@angular/animations';
@Component({
  templateUrl: 'list.component.html',
  animations: [
    trigger('listAnimation', [
    ...
    ])
  ]
})
class ListComponent {
  items = [];

  showItems() {
    this.items = [0,1,2,3,4];
  }

  hideItems() {
    this.items = [];
  }

  toggle() {
    this.items.length ? this.hideItems() : this.showItems();
   }
 }
```

Here is the animation trigger code:

```
trigger('listAnimation', [
  transition('* => *', [ // each time the binding value changes
    query(':leave', [
      stagger(100, [
        animate('0.5s', style({ opacity: 0 }))
      ])
    ]),
    query(':enter', [
      style({ opacity: 0 }),
      stagger(100, [
        animate('0.5s', style({ opacity: 1 }))
      ])
    ])
  ])
])
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/animations/stagger>
