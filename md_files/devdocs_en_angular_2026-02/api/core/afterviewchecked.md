# AfterViewChecked

AfterViewChecked



# AfterViewChecked

A lifecycle hook that is called after the default change detector has completed checking a component's view for changes.

[AfterContentChecked](aftercontentchecked)[Lifecycle hooks guide](../../guide/components/lifecycle)

## API

```
interface AfterViewChecked {
  ngAfterViewChecked(): void;
}
```

### ngAfterViewChecked

`void`

A callback method that is invoked immediately after the default change detector has completed one change-check cycle for a component's view.

@returns`void`

## Usage Notes

The following snippet shows how a component can implement this interface to define its own after-check functionality.

```
@Component({
        selector: 'my-cmp',
        template: `...`,
        standalone: false,
      })
      class MyComponent implements AfterViewChecked {
        ngAfterViewChecked() {
          // ...
        }
      }
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/AfterViewChecked>
