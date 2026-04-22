# AfterContentChecked

AfterContentChecked



# AfterContentChecked

A lifecycle hook that is called after the default change detector has completed checking all content of a directive. It will run after the content has been checked and most of the time it's during a change detection cycle.

[AfterViewChecked](afterviewchecked)[Lifecycle hooks guide](../../guide/components/lifecycle)

## API

```
interface AfterContentChecked {
  ngAfterContentChecked(): void;
}
```

### ngAfterContentChecked

`void`

A callback method that is invoked immediately after the default change detector has completed checking all of the directive's content.

@returns`void`

## Usage Notes

The following snippet shows how a component can implement this interface to define its own after-check functionality.

```
@Component({
        selector: 'my-cmp',
        template: `...`,
        standalone: false,
      })
      class MyComponent implements AfterContentChecked {
        ngAfterContentChecked() {
          // ...
        }
      }
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/AfterContentChecked>
