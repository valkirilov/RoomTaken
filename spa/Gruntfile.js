module.exports = function(grunt) {

	grunt.initConfig({
		pkg : grunt.file.readJSON('package.json'),
        nggettext_extract: {
            pot: {
                files: {
                    'app/po/template.pot': ['app/*.html', 'app/partials/*.html']
                }
            },
        },
        nggettext_compile: {
            all: {
                files: {
                    'app/js/translations.js': ['app/po/*.po']
                }
            },
        },
	});

    grunt.loadNpmTasks('grunt-angular-gettext');

    grunt.registerTask('default', ['nggettext_extract', 'nggettext_compile']);
};
