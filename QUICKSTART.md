# Shadcn Theme - Quick Start Guide

## Installation (3 Steps)

### Step 1: Copy Theme
```bash
cp -r theme_shadcn /path/to/odoo/addons/
```

### Step 2: Restart Odoo
```bash
sudo systemctl restart odoo
# or
./odoo-bin -c odoo.conf
```

### Step 3: Install in Odoo
1. Go to **Apps** menu
2. Click **Update Apps List**
3. Search for **"Shadcn"**
4. Click **Install**
5. Go to **Website > Configuration > Settings**
6. Select **Shadcn Theme**
7. Save

## Usage

### Adding Snippets to Pages

1. Navigate to your website
2. Click **Edit** (top-right)
3. Click **Blocks** (left sidebar)
4. Find Shadcn snippets:
   - Shadcn Hero Section
   - Shadcn Features Section  
   - Shadcn Call to Action
   - Shadcn Statistics
5. Drag and drop onto your page
6. Click **Save**

### Customizing Colors

Edit `theme_shadcn/static/src/scss/primary_variables.scss`:

```scss
$o-color-palettes: map-merge($o-color-palettes, (
    'primary': (
        '500': #YOUR_BRAND_COLOR,  // Change this
    ),
));
```

Then restart Odoo.

### Customizing Typography

Edit `theme_shadcn/static/src/scss/primary_variables.scss`:

```scss
$o-theme-font-family: 'YourFont', sans-serif;
```

Update the Google Fonts import in `theme.scss`:

```scss
@import url('https://fonts.googleapis.com/css2?family=YourFont:wght@300;400;700&display=swap');
```

## Common Customizations

### Change Primary Color
File: `static/src/scss/primary_variables.scss`
Line: Search for `'primary': (`
Change: `'500': #0ea5e9` to your color

### Change Font
File: `static/src/scss/primary_variables.scss`
Line: `$o-theme-font-family`
Change: Replace `'Inter'` with your font

### Adjust Spacing
File: `static/src/scss/theme.scss`
Search: Section padding classes (`.hero`, `.features`, etc.)
Change: `padding: 6rem 0` to your preferred value

### Modify Border Radius
File: `static/src/scss/primary_variables.scss`
Lines: `$border-radius*` variables
Change: Values from `0.5rem` to your preference

### Add Custom Snippet

1. Edit `views/snippets.xml`
2. Add new template:
```xml
<template id="s_my_snippet" name="My Snippet">
    <section class="s_my_snippet">
        <!-- Your HTML -->
    </section>
</template>
```
3. Register in menu:
```xml
<t t-snippet="theme_shadcn.s_my_snippet" 
   t-thumbnail="/theme_shadcn/static/src/img/snippets/my.svg"/>
```
4. Add styles in `static/src/scss/theme.scss`

## Troubleshooting

### Theme not showing in Apps
- Verify folder is in addons directory
- Check `__manifest__.py` syntax
- Update apps list
- Check Odoo logs: `/var/log/odoo/odoo.log`

### Styles not loading
- Clear browser cache (Ctrl+Shift+Del)
- Restart Odoo server
- Check browser console for errors (F12)

### Snippets not appearing
- Ensure theme is installed AND activated
- Verify you're in edit mode on website
- Check XML syntax in `views/snippets.xml`

## File Locations

| What | File Path |
|------|-----------|
| Colors | `static/src/scss/primary_variables.scss` |
| Styles | `static/src/scss/theme.scss` |
| JavaScript | `static/src/js/theme.js` |
| Header/Footer | `views/assets.xml` |
| Snippets | `views/snippets.xml` |
| Options | `views/options.xml` |

## Support

- 📖 Full docs: `README.md`
- 📋 Installation: `INSTALLATION.md`
- 📝 Details: `PROJECT_SUMMARY.md`
- 🎨 Preview: `static/description/preview.html`

## Tips

✅ Always test in development first
✅ Keep backups before customizing
✅ Use Git for version control
✅ Check browser console for errors
✅ Restart Odoo after SCSS changes

## Version

- **Theme Version**: 18.0.1.0.0
- **Odoo Version**: 18.0
- **License**: LGPL-3
