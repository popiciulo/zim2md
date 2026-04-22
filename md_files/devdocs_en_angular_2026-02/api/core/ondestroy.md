# OnDestroy

OnDestroy



# OnDestroy

A lifecycle hook that is called when a directive, pipe, or service is destroyed. Use for any custom cleanup that needs to occur when the instance is destroyed.

[Lifecycle hooks guide](../../guide/components/lifecycle)

## API

```
interface OnDestroy {
  ngOnDestroy(): void;
}
```

### ngOnDestroy

`void`

A callback method that performs custom clean-up, invoked immediately before a directive, pipe, or service instance is destroyed.

@returns`void`

## Usage Notes

The following snippet shows how a component can implement this interface to define its own custom clean-up method.

```
@Component({
        selector: 'my-cmp',
        template: `...`,
        standalone: false,
      })
      class MyComponent implements OnDestroy {
        ngOnDestroy() {
          // ...
        }
      }
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/OnDestroy>
