# TemplateRef

TemplateRef



# TemplateRef

Represents an embedded template that can be used to instantiate embedded views. To instantiate embedded views based on a template, use the [`ViewContainerRef`](viewcontainerref) method `createEmbeddedView()`.

[ViewContainerRef](viewcontainerref)

## API

```
class TemplateRef<C> {
  constructor(_declarationLView: LView<unknown>, _declarationTContainer: TContainerNode, elementRef: ElementRef<any>): TemplateRef<C>;
  readonly elementRef: ElementRef<any>;
  createEmbeddedView(context: C, injector?: Injector | undefined): EmbeddedViewRef<C>;
}
```

### constructor

`TemplateRef<C>`

@param\_declarationLView`LView<unknown>`

@param\_declarationTContainer`TContainerNode`

@paramelementRef`ElementRef<any>`

@returns`TemplateRef<C>`

### elementRef

`ElementRef<any>`

The anchor element in the parent view for this embedded view.

The data-binding and [injection contexts](../../guide/di/dependency-injection-context) of embedded views created from this [`TemplateRef`](templateref) inherit from the contexts of this location.

Typically new embedded views are attached to the view container of this location, but in advanced use-cases, the view can be attached to a different container while keeping the data-binding and injection context from the original location.

### createEmbeddedView

`EmbeddedViewRef<C>`

Instantiates an unattached embedded view based on this template.

@paramcontext`C`

The data-binding context of the embedded view, as declared in the `<ng-template>` usage.

@paraminjector`Injector | undefined`

Injector to be used within the embedded view.

@returns`EmbeddedViewRef<C>`

## Description

Represents an embedded template that can be used to instantiate embedded views. To instantiate embedded views based on a template, use the [`ViewContainerRef`](viewcontainerref) method `createEmbeddedView()`.

Access a [`TemplateRef`](templateref) instance by placing a directive on an `<ng-template>` element (or directive prefixed with `*`). The [`TemplateRef`](templateref) for the embedded view is injected into the constructor of the directive, using the [`TemplateRef`](templateref) token.

You can also use a [`Query`](query) to find a [`TemplateRef`](templateref) associated with a component or a directive.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/TemplateRef>
