# DoCheck

DoCheck



# DoCheck

A lifecycle hook that invokes a custom change-detection function for a directive, in addition to the check performed by the default change-detector.

[OnChanges](onchanges)[Lifecycle hooks guide](../../guide/components/lifecycle)

## API

```
interface DoCheck {
  ngDoCheck(): void;
}
```

### ngDoCheck

`void`

A callback method that performs change-detection, invoked after the default change-detector runs. See [`KeyValueDiffers`](keyvaluediffers) and [`IterableDiffers`](iterablediffers) for implementing custom change checking for collections.

@returns`void`

## Description

A lifecycle hook that invokes a custom change-detection function for a directive, in addition to the check performed by the default change-detector.

The default change-detection algorithm looks for differences by comparing bound-property values by reference across change detection runs. You can use this hook to check for and respond to changes by some other means.

When the default change detector detects changes, it invokes `ngOnChanges()` if supplied, regardless of whether you perform additional change detection. Typically, you should not use both [`DoCheck`](docheck) and [`OnChanges`](onchanges) to respond to changes on the same input.

## Usage Notes

The following snippet shows how a component can implement this interface to invoke it own change-detection cycle.

```
@Component({
        selector: 'my-cmp',
        template: `...`,
        standalone: false,
      })
      class MyComponent implements DoCheck {
        ngDoCheck() {
          // ...
        }
      }
```

For a more complete example and discussion, see [Defining custom change detection](../../guide/components/lifecycle#defining-custom-change-detection).

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/DoCheck>
