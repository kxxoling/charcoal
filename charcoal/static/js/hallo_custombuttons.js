// Copied from: https://jossingram.wordpress.com/2014/07/24/add-some-blockquote-buttons-to-wagtail-cms-wysiwyg-editor/
(function() {
  (function($) {
    return $.widget('IKS.blockquotebutton', {
      options: {
        uuid: '',
        editable: null
      },
      populateToolbar: function(toolbar) {
        var button, widget;

        widget = this;

        button = $('<span></span>');
        button.hallobutton({
          uuid: this.options.uuid,
          editable: this.options.editable,
          label: 'Blockquote',
          icon: 'fa fa-quote-left',
          command: null
        });

        toolbar.append(button);

        button.on('click', function(event) {
          return widget.options.editable.execute('formatBlock', 'blockquote');
        });
      }
    });
  })(jQuery);
}).call(this);

