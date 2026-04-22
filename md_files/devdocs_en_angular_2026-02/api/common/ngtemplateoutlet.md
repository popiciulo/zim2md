# NgTemplateOutlet

NgTemplateOutlet



# NgTemplateOutlet

Inserts an embedded view from a prepared [`TemplateRef`](../core/templateref).

## API

```
class NgTemplateOutlet<C = unknown> implements OnChanges {
  constructor(_viewContainerRef: ViewContainerRef): NgTemplateOutlet<C>;
  @Input() ngTemplateOutletContext: C | null | undefined;
  @Input() ngTemplateOutlet: TemplateRef<C> | null | undefined;
  @Input() ngTemplateOutletInjector: Injector | null | undefined;
}
```

### constructor

`NgTemplateOutlet<C>`

@param\_viewContainerRef`ViewContainerRef`

@returns`NgTemplateOutlet<C>`

### ngTemplateOutletContext

`C | null | undefined`

A context object to attach to the [`EmbeddedViewRef`](../core/embeddedviewref). This should be an object, the object's keys will be available for binding by the local template `let` declarations. Using the key `$implicit` in the context object will set its value as default.

### ngTemplateOutlet

`TemplateRef<C> | null | undefined`

A string defining the template reference and optionally the context object for the template.

### ngTemplateOutletInjector

`Injector | null | undefined`

Injector to be used within the embedded view.

### ngOnChanges

`void`

@paramchanges`{ [propName: string]: SimpleChange<any>; }`

@returns`void`

## Description

Inserts an embedded view from a prepared [`TemplateRef`](../core/templateref).

You can attach a context object to the [`EmbeddedViewRef`](../core/embeddedviewref) by setting `[ngTemplateOutletContext]`. `[ngTemplateOutletContext]` should be an object, the object's keys will be available for binding by the local template `let` declarations.

---

## Exported by

- `CommonModule`

## Usage Notes

```
<ng-container *ngTemplateOutlet="templateRefExp; context: contextExp"></ng-container>
```

Using the key `$implicit` in the context object will set its value as default.

### Example

```
@Component({
  selector: 'ng-template-outlet-example',
  imports: [NgTemplateOutlet],
  template: `
    <ng-container *ngTemplateOutlet="greet"></ng-container>
    <hr />
    <ng-container *ngTemplateOutlet="eng; context: myContext"></ng-container>
    <hr />
    <ng-container *ngTemplateOutlet="svk; context: myContext"></ng-container>
    <hr />

    <ng-template #greet><span>Hello</span></ng-template>
    <ng-template #eng let-name
      ><span>Hello {{ name }}!</span></ng-template
    >
    <ng-template #svk let-person="localSk"
      ><span>Ahoj {{ person }}!</span></ng-template
    >
  `,
})
export class NgTemplateOutletExample {
  myContext = {$implicit: 'World', localSk: 'Svet'};
}
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/NgTemplateOutlet>
