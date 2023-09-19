function toggleSidebar(id) {
    // animated the left side bar to move in and out of the screen and updates the html tags accordingly.
    var elem = document.getElementById(id);
    var classes = elem.className.split(' ');
    var collapsed = classes.indexOf('collapsed') !== -1;
    var padding = {};

    if (collapsed) {
        classes.splice(classes.indexOf('collapsed'), 1);
        padding[id] = 300;
    } else {
        padding[id] = 0;
        classes.push('collapsed');
    }
    elem.className = classes.join(' ');
}