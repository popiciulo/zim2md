# forwardRef

forwardRef



# forwardRef

Allows to refer to references which are not yet defined.

[Resolve circular dependencies with a forward reference](../../guide/di/di-in-action#resolve-circular-dependencies-with-a-forward-reference)

## API

```
function forwardRef(forwardRefFn: ForwardRefFn): Type<any>;
```

### forwardRef

`Type<any>`

Allows to refer to references which are not yet defined.

For instance, [`forwardRef`](forwardref) is used when the `token` which we need to refer to for the purposes of DI is declared, but not yet defined. It is also used when the `token` which we use when creating a query is not yet defined.

[`forwardRef`](forwardref) is also used to break circularities in standalone components imports.

@paramforwardRefFn`ForwardRefFn`

@returns`Type<any>`

Usage notes

### Circular dependency example

{@example core/di/ts/forward\_ref/forward\_ref\_spec.ts region='forward\_ref'}

### Circular standalone reference import example

```
@Component({
  imports: [ChildComponent],
  selector: 'app-parent',
  template: `<app-child [hideParent]="hideParent()"></app-child>`,
})
export class ParentComponent {
   hideParent = input.required<boolean>();
}


@Component({
  imports: [forwardRef(() => ParentComponent)],
  selector: 'app-child',
  template: `
   @if(!hideParent() {
      <app-parent/>
   }
 `,
})
export class ChildComponent {
   hideParent = input.required<boolean>();
}
```

## Description

Allows to refer to references which are not yet defined.

For instance, [`forwardRef`](forwardref) is used when the `token` which we need to refer to for the purposes of DI is declared, but not yet defined. It is also used when the `token` which we use when creating a query is not yet defined.

[`forwardRef`](forwardref) is also used to break circularities in standalone components imports.

## Usage Notes

### Circular dependency example

```
@Injectable()
      class Door {
        lock: Lock;

        // Door attempts to inject Lock, despite it not being defined yet.
        // forwardRef makes this possible.
        constructor(@Inject(forwardRef(() => Lock)) lock: Lock) {
          this.lock = lock;
        }
      }

      // Only at this point Lock is defined.
      class Lock {}

      const injector = Injector.create({
        providers: [
          {provide: Lock, deps: []},
          {provide: Door, deps: [Lock]},
        ],
      });

      expect(injector.get(Door) instanceof Door).toBe(true);
      expect(injector.get(Door).lock instanceof Lock).toBe(true);
```

### Circular standalone reference import example

```
@Component({
  imports: [ChildComponent],
  selector: 'app-parent',
  template: `<app-child [hideParent]="hideParent()"></app-child>`,
})
export class ParentComponent {
   hideParent = input.required<boolean>();
}


@Component({
  imports: [forwardRef(() => ParentComponent)],
  selector: 'app-child',
  template: `
   @if(!hideParent() {
      <app-parent/>
   }
 `,
})
export class ChildComponent {
   hideParent = input.required<boolean>();
}
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/forwardRef>
