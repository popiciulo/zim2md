# DomSanitizer

DomSanitizer



# DomSanitizer

DomSanitizer helps preventing Cross Site Scripting Security bugs (XSS) by sanitizing values to be safe to use in the different DOM contexts.

## API

```
abstract class DomSanitizer implements Sanitizer {
  abstract sanitize(context: SecurityContext, value: string | SafeValue | null): string | null;
  abstract bypassSecurityTrustHtml(value: string): SafeHtml;
  abstract bypassSecurityTrustStyle(value: string): SafeStyle;
  abstract bypassSecurityTrustScript(value: string): SafeScript;
  abstract bypassSecurityTrustUrl(value: string): SafeUrl;
  abstract bypassSecurityTrustResourceUrl(value: string): SafeResourceUrl;
}
```

### sanitize

`string | null`

Gets a safe value from either a known safe value or a value with unknown safety.

If the given value is already a [`SafeValue`](safevalue), this method returns the unwrapped value. If the security context is HTML and the given value is a plain string, this method sanitizes the string, removing any potentially unsafe content. For any other security context, this method throws an error if provided with a plain string.

@paramcontext`SecurityContext`

@paramvalue`string | SafeValue | null`

@returns`string | null`

### bypassSecurityTrustHtml

`SafeHtml`

Bypass security and trust the given value to be safe HTML. Only use this when the bound HTML is unsafe (e.g. contains `<script>` tags) and the code should be executed. The sanitizer will leave safe HTML intact, so in most situations this method should not be used.

**WARNING:** calling this method with untrusted user data exposes your application to XSS security risks!

@paramvalue`string`

@returns`SafeHtml`

### bypassSecurityTrustStyle

`SafeStyle`

Bypass security and trust the given value to be safe style value (CSS).

**WARNING:** calling this method with untrusted user data exposes your application to XSS security risks!

@paramvalue`string`

@returns`SafeStyle`

### bypassSecurityTrustScript

`SafeScript`

Bypass security and trust the given value to be safe JavaScript.

**WARNING:** calling this method with untrusted user data exposes your application to XSS security risks!

@paramvalue`string`

@returns`SafeScript`

### bypassSecurityTrustUrl

`SafeUrl`

Bypass security and trust the given value to be a safe style URL, i.e. a value that can be used in hyperlinks or `<img src>`.

**WARNING:** calling this method with untrusted user data exposes your application to XSS security risks!

@paramvalue`string`

@returns`SafeUrl`

### bypassSecurityTrustResourceUrl

`SafeResourceUrl`

Bypass security and trust the given value to be a safe resource URL, i.e. a location that may be used to load executable code from, like `<script src>`, or `<iframe src>`.

**WARNING:** calling this method with untrusted user data exposes your application to XSS security risks!

@paramvalue`string`

@returns`SafeResourceUrl`

## Description

DomSanitizer helps preventing Cross Site Scripting Security bugs (XSS) by sanitizing values to be safe to use in the different DOM contexts.

For example, when binding a URL in an `<a [href]="someValue">` hyperlink, `someValue` will be sanitized so that an attacker cannot inject e.g. a `javascript:` URL that would execute code on the website.

In specific situations, it might be necessary to disable sanitization, for example if the application genuinely needs to produce a `javascript:` style link with a dynamic value in it. Users can bypass security by constructing a value with one of the `bypassSecurityTrust...` methods, and then binding to that value from the template.

These situations should be very rare, and extraordinary care must be taken to avoid creating a Cross Site Scripting (XSS) security bug!

When using `bypassSecurityTrust...`, make sure to call the method as early as possible and as close as possible to the source of the value, to make it easy to verify no security bug is created by its use.

It is not required (and not recommended) to bypass security if the value is safe, e.g. a URL that does not start with a suspicious protocol, or an HTML snippet that does not contain dangerous code. The sanitizer leaves safe values intact.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/platform-browser/DomSanitizer>
