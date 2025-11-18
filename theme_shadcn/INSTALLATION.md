# Shadcn Theme - Installation & Usage Guide

## Prerequisites

- Odoo 18 installed and running
- Access to Odoo Apps menu (admin rights)
- Basic understanding of Odoo website builder

## Installation Steps

### Method 1: Direct Installation (Recommended)

1. **Copy the theme to your addons directory**
   ```bash
   cp -r theme_shadcn /path/to/odoo/addons/
   ```

2. **Restart Odoo server**
   ```bash
   sudo systemctl restart odoo
   # or
   ./odoo-bin -c /path/to/odoo.conf
   ```

3. **Update Apps List**
   - Log in to Odoo
   - Go to Apps menu
   - Click "Update Apps List" (you may need to activate Developer Mode)
   - Confirm the update

4. **Install the Theme**
   - In Apps menu, search for "Shadcn"
   - Click "Install" on "Shadcn Theme"

5. **Activate the Theme**
   - Go to Website > Configuration > Settings
   - In the "Website Theme" section, select "Shadcn Theme"
   - Save changes

### Method 2: Using Odoo Configuration

1. Add the theme directory to your `odoo.conf` file:
   ```ini
   [options]
   addons_path = /path/to/odoo/addons,/path/to/theme_shadcn
   ```

2. Follow steps 2-5 from Method 1

## Usage Guide

### Using Website Builder Snippets

1. **Access Website Editor**
   - Go to your website
   - Click "Edit" button in the top-right corner

2. **Add Snippets**
   - Click the "Blocks" button in the left sidebar
   - Look for Shadcn snippets:
     * Shadcn Hero Section
     * Shadcn Features Section
     * Shadcn Call to Action
     * Shadcn Statistics
   - Drag and drop them onto your page

3. **Customize Snippets**
   - Click on any snippet
   - Use the options panel to customize colors, layout, and content
   - Edit text directly by clicking on it

### Customizing the Header

1. Go to Website > Configuration > Menu Editor
2. Enable "Shadcn Header" template
3. Customize menu items as needed

### Customizing the Footer

1. Edit the footer template in Website > Configuration > Menu Editor
2. Enable "Shadcn Footer" template
3. Update links and social media icons

### Color Customization

To change the theme colors:

1. Edit `theme_shadcn/static/src/scss/primary_variables.scss`
2. Modify the color values in the `$o-color-palettes` map
3. Restart Odoo server to see changes

Example:
```scss
$o-color-palettes: map-merge($o-color-palettes, (
    'primary': (
        '500': #YOUR_COLOR_HERE,
    ),
));
```

### Typography Customization

To use a different font:

1. Edit `theme_shadcn/static/src/scss/primary_variables.scss`
2. Change the `$o-theme-font-family` variable
3. Update the Google Fonts import in `theme_shadcn/static/src/scss/theme.scss`

## Features Overview

### Header
- Clean, modern navigation
- Responsive mobile menu
- Sticky header on scroll
- Smooth backdrop blur effect

### Snippets

#### Hero Section
- Large heading area
- Call-to-action buttons
- Optional badge
- Image/illustration support
- Customizable layout (left, center, right)

#### Features Section
- Grid layout (2, 3, or 4 columns)
- Icon support
- Hover effects
- Responsive on all devices

#### Call to Action
- Gradient background
- Large button
- Conversion-focused design

#### Statistics
- Display key metrics
- 4-column layout
- Animated numbers (with custom JS)

### Styling Components

- **Buttons**: Primary, Secondary, Outline variants
- **Cards**: Hover effects, shadows
- **Forms**: Modern input fields with focus states
- **Badges**: Multiple color schemes
- **Typography**: Optimized font sizes and weights

## Troubleshooting

### Theme not appearing in Apps

1. Check if the theme folder is in the correct addons directory
2. Verify the `__manifest__.py` file has correct syntax
3. Update the apps list
4. Check Odoo logs for errors

### Styles not loading

1. Clear browser cache
2. Restart Odoo server
3. Check if SCSS files have correct syntax
4. Verify assets are properly defined in `__manifest__.py`

### Snippets not showing

1. Make sure the theme is installed AND activated
2. Check if you're in website edit mode
3. Verify XML files are valid
4. Check Odoo logs for template errors

## Advanced Customization

### Adding Custom Snippets

1. Create a new template in `views/snippets.xml`:
   ```xml
   <template id="s_custom_snippet" name="Custom Snippet">
       <section class="s_custom">
           <!-- Your HTML here -->
       </section>
   </template>
   ```

2. Register it in the snippets menu:
   ```xml
   <t t-snippet="theme_shadcn.s_custom_snippet" 
      t-thumbnail="/theme_shadcn/static/src/img/snippets/custom.svg"/>
   ```

3. Add styles in `static/src/scss/theme.scss`

### Adding Custom JavaScript

Add your custom JavaScript in `static/src/js/theme.js` or create new JS files and register them in `__manifest__.py`:

```python
'assets': {
    'web.assets_frontend': [
        'theme_shadcn/static/src/js/custom.js',
    ],
},
```

## Best Practices

1. **Always test changes in development environment first**
2. **Keep backups before major customizations**
3. **Use Git for version control**
4. **Document custom changes**
5. **Test on multiple devices and browsers**

## Support & Resources

- Theme Documentation: See README.md
- Odoo Documentation: https://www.odoo.com/documentation/18.0/
- shadcn/ui Design System: https://ui.shadcn.com/

## Version Compatibility

- Odoo 18.0 and above
- May work with Odoo 17.0 with minor modifications

## License

LGPL-3 - See LICENSE file for details
