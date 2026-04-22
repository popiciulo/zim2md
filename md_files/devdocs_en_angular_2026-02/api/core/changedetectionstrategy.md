# ChangeDetectionStrategy

ChangeDetectionStrategy



# ChangeDetectionStrategy

The strategy that the default change detector uses to detect changes. When set, takes effect the next time change detection is triggered.

[Change detection usage](changedetectorref?tab=usage-notes)[Skipping component subtrees](https://angular.dev/best-practices/skipping-subtrees)

## API

```
enum ChangeDetectionStrategy {
  OnPush: ChangeDetectionStrategy.OnPush;
  Default: ChangeDetectionStrategy.Default;
}
```

### OnPush

Use the `CheckOnce` strategy, meaning that automatic change detection is deactivated until reactivated by setting the strategy to `Default` (`CheckAlways`). Change detection can still be explicitly invoked. This strategy applies to all child directives and cannot be overridden.

### Default

Use the default `CheckAlways` strategy, in which change detection is automatic until explicitly deactivated.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/ChangeDetectionStrategy>
