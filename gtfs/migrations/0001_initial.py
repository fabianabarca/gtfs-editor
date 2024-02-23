# Generated by Django 4.2.5 on 2024-02-01 17:35

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('agency_id', models.CharField(help_text='Identificador único de la agencia de transportes.', max_length=127)),
                ('name', models.CharField(help_text='Nombre completo de la agencia de transportes.', max_length=255)),
                ('url', models.URLField(help_text='URL de la agencia de transportes.')),
                ('timezone', models.CharField(help_text='Zona horaria de la agencia de transportes.', max_length=255)),
                ('lang', models.CharField(help_text='Código ISO 639-1 de idioma primario.', max_length=2)),
                ('phone', models.CharField(help_text='Número de teléfono.', max_length=255)),
                ('fare_url', models.URLField(help_text='URL para la compra de tiquetes en línea.')),
                ('email', models.EmailField(help_text='Correo electrónico de servicio al cliente.', max_length=254)),
            ],
            options={
                'verbose_name': 'agency',
                'verbose_name_plural': 'agencies',
            },
        ),
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('id', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('service_id', models.CharField(db_index=True, help_text='Indentificador único de un calendario.', max_length=255)),
                ('monday', models.CharField(choices=[('1', 'El servicio sí está disponible los lunes incluidos en este período.'), ('0', 'El servcio no está disponible los lunes incluidos en este período.')], help_text='¿El servicio está disponible los lunes?', max_length=1)),
                ('tuesday', models.CharField(choices=[('1', 'El servicio sí está disponible los martes incluidos en este período.'), ('0', 'El servcio no está disponible los martes incluidos en este período.')], help_text='¿El servicio está disponible los martes?', max_length=1)),
                ('wednesday', models.CharField(choices=[('1', 'El servicio sí está disponible los miércoles incluidos en este período.'), ('0', 'El servcio no está disponible los miércoles incluidos en este período.')], help_text='¿El servicio está disponible los miércoles?', max_length=1)),
                ('thursday', models.CharField(choices=[('1', 'El servicio sí está disponible los jueves incluidos en este período.'), ('0', 'El servcio no está disponible los jueves incluidos en este período.')], help_text='¿El servicio está disponible los jueves?', max_length=1)),
                ('friday', models.CharField(choices=[('1', 'El servicio sí está disponible los viernes incluidos en este período.'), ('0', 'El servcio no está disponible los viernes incluidos en este período.')], help_text='¿El servicio está disponible los viernes?', max_length=1)),
                ('saturday', models.CharField(choices=[('1', 'El servicio sí está disponible los sábados incluidos en este período.'), ('0', 'El servcio no está disponible los sábados incluidos en este período.')], help_text='¿El servicio está disponible los sábados?', max_length=1)),
                ('sunday', models.CharField(choices=[('1', 'El servicio sí está disponible los domingos incluidos en este período.'), ('0', 'El servcio no está disponible los domingos incluidos en este período.')], help_text='¿El servicio está disponible los domingos?', max_length=1)),
                ('start_date', models.DateField(default=None, help_text='Inicio de la vigencia del horario.')),
                ('end_date', models.DateField(default=None, help_text='Fin de la vigencia del horario.')),
            ],
            options={
                'verbose_name': 'calendar',
                'verbose_name_plural': 'calendars',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('company_id', models.CharField(blank=True, max_length=255, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=127)),
                ('address', models.CharField(max_length=1024)),
                ('phone', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('website', models.URLField(blank=True)),
                ('logo', models.ImageField(blank=True, upload_to='logos/')),
            ],
        ),
        migrations.CreateModel(
            name='FareAttribute',
            fields=[
                ('id', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('fare_id', models.CharField(db_index=True, help_text='Identificador único de la clase de tarifa.', max_length=255)),
                ('price', models.IntegerField(help_text='Precio de tarifa, en unidades especificadas en currency_type')),
                ('currency_type', models.CharField(help_text='Código ISO 4217, alfabético de moneda: CRC.', max_length=3)),
                ('payment_method', models.IntegerField(choices=[(0, 'La tarifa se paga abordo.'), (1, 'La tarifa se paga previo a subir al transporte.')], default=1, help_text='¿Cuándo se paga la tarifa?')),
                ('transfers', models.IntegerField(blank=True, choices=[(0, 'No se permiten transferencias en esta tarifa.'), (1, 'Los pasajeros pueden transferir una vez.'), (2, 'Los pasajeros pueden transferir dos veces.'), (None, 'Se pueden realizar transferencias ilimitadas.')], default=None, help_text='¿Se permiten las transferencias?', null=True)),
                ('transfer_duration', models.IntegerField(blank=True, help_text='Tiempo en segundos hasta que un tiquete o transferencia expira.', null=True)),
                ('agency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gtfs.agency')),
            ],
            options={
                'verbose_name': 'fare attribute',
                'verbose_name_plural': 'fare attributes',
            },
        ),
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('feed_id', models.CharField(blank=True, max_length=255, primary_key=True, serialize=False)),
                ('zip_file', models.FileField(upload_to='feeds/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_current', models.BooleanField(default=True)),
                ('in_edition', models.BooleanField(default=False)),
                ('company_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gtfs.company')),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('route_id', models.CharField(db_index=True, help_text='Identificador único de la ruta.', max_length=64)),
                ('short_name', models.CharField(help_text='Nombre corto de la ruta.', max_length=63)),
                ('long_name', models.CharField(help_text='Nombre largo de la ruta.', max_length=255)),
                ('desc', models.TextField(blank=True, help_text='Descripción detallada de la ruta.', verbose_name='description')),
                ('route_type', models.IntegerField(choices=[(0, 'Tranvía o tren ligero'), (1, 'Subterráneo o metro'), (2, 'Ferrocarril'), (3, 'Bus'), (4, 'Ferry'), (5, 'Teleférico'), (6, 'Góndola'), (7, 'Funicular')], default=3, help_text='Medio de transporte usado en la ruta.', verbose_name='route type')),
                ('url', models.CharField(blank=True, help_text='Página web de la ruta.', max_length=64)),
                ('color', models.CharField(blank=True, help_text='Color de la ruta en código hexadecimal.', max_length=6)),
                ('text_color', models.CharField(blank=True, help_text='Color del texto de ruta en código hexadecimal.', max_length=6)),
                ('agency', models.ForeignKey(blank=True, help_text='Agencia de transportes de la ruta.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='gtfs.agency')),
                ('feed_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gtfs.feed')),
            ],
            options={
                'verbose_name': 'route',
                'verbose_name_plural': 'routes',
            },
        ),
        migrations.CreateModel(
            name='Shape',
            fields=[
                ('id', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('shape_id', models.CharField(help_text='Identificador único de una trayectoria.', max_length=255)),
                ('pt_lat', models.DecimalField(decimal_places=16, help_text='Latitud WGS 84 de punto de la trayectoria.', max_digits=22)),
                ('pt_lon', models.DecimalField(decimal_places=16, help_text='Longitud WGS 84 de punto de la trayectoria.', max_digits=22)),
                ('pt_sequence', models.PositiveIntegerField(help_text='Secuencia en la que los puntos de la trayectoria se conectan para crear la forma o geometría')),
                ('dist_traveled', models.DecimalField(blank=True, decimal_places=3, default=0.0, help_text='La unidad es km, la precisión es en metros (0.001 km)', max_digits=6, null=True)),
                ('feed_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gtfs.feed')),
            ],
            options={
                'verbose_name': 'shape',
                'verbose_name_plural': 'shapes',
            },
        ),
        migrations.CreateModel(
            name='Stop',
            fields=[
                ('id', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('stop_id', models.CharField(db_index=True, help_text='Identificador único de una parada o estación.', max_length=255)),
                ('name', models.CharField(help_text='Nombre de la parada.', max_length=255)),
                ('desc', models.CharField(blank=True, help_text='Descripción de la parada.', max_length=255, verbose_name='description')),
                ('lat', models.DecimalField(decimal_places=16, help_text='Latitud WGS 84 de la parada o estación.', max_digits=22)),
                ('lon', models.DecimalField(decimal_places=16, help_text='Longitud WGS 84 de la parada o estación.', max_digits=22)),
                ('loc', django.contrib.gis.db.models.fields.PointField(blank=True, help_text='Ubicación de la parada o estación.', null=True, srid=4326)),
                ('url', models.URLField(blank=True, help_text='URL de la parada.')),
                ('location_type', models.CharField(blank=True, choices=[('0', 'Parada'), ('1', 'Estación')], help_text='¿Es una parada o una estación?', max_length=1)),
                ('parent_station', models.CharField(blank=True, help_text='La estación asociada con la parada.', max_length=255, null=True)),
                ('wheelchair_boarding', models.CharField(blank=True, choices=[('0', 'No hay información.'), ('1', 'Abordaje parcial de silla de ruedas.'), ('2', 'Las sillas de ruedas no pueden subir.')], help_text='¿Es posible subir al transporte en silla de ruedas?', max_length=1, null=True)),
                ('feed_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gtfs.feed')),
            ],
            options={
                'verbose_name': 'stop',
                'verbose_name_plural': 'stops',
            },
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('zone_id', models.CharField(choices=[('SGAB_A', 'San Gabriel A'), ('SGAB_B', 'San Gabriel B'), ('SGAB_C', 'San Gabriel C'), ('SGAB_D', 'San Gabriel D'), ('ACOS_A', 'Acosta A'), ('ACOS_B', 'Acosta B'), ('ACOS_C', 'Acosta C'), ('ACOS_D', 'Acosta D'), ('RUTA_E', 'Ruta E'), ('RUTA_F', 'Ruta F'), ('RUTA_G', 'Ruta G')], db_index=True, help_text='Identificador único de una zona.', max_length=63)),
                ('feed_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gtfs.feed')),
            ],
            options={
                'verbose_name': 'zone',
                'verbose_name_plural': 'zones',
            },
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('trip_id', models.CharField(db_index=True, help_text='Indentificador único de viaje.', max_length=255)),
                ('headsign', models.CharField(blank=True, help_text='Identificación de destino para pasajeros.', max_length=255)),
                ('short_name', models.CharField(blank=True, help_text='Nombre corto utilizado en horarios y letreros.', max_length=63)),
                ('departure_time', models.TimeField(blank=True, default=None, help_text='Hora de salida del viaje (ELIMINAR).', null=True)),
                ('arrival_time', models.TimeField(blank=True, default=None, help_text='Hora de llegada del viaje (ELIMINAR).', null=True)),
                ('duration', models.PositiveIntegerField(blank=True, default=None, help_text='Minutos de duración del viaje.', null=True)),
                ('direction', models.CharField(blank=True, choices=[('0', 'Hacia San José.'), ('1', 'Desde San José.')], help_text='Dirección para rutas en dos sentidos.', max_length=1)),
                ('wheelchair_accessible', models.CharField(blank=True, choices=[('0', 'No hay información.'), ('1', 'Hay espacio para el transporte de sillas de ruedas.'), ('2', 'No hay espacio para el transporte de sillas de ruedas.')], help_text='¿Hay espacio para el transporte de sillas de ruedas?', max_length=1)),
                ('bikes_allowed', models.CharField(blank=True, choices=[('0', 'No hay información.'), ('1', 'Hay espacio para el transporte de bicicletas.'), ('2', 'No hay espacio para el transporte de bicicletas.')], help_text='¿Hay espacio para el transporte de bicicletas?', max_length=1)),
                ('feed_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gtfs.feed')),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gtfs.route')),
                ('service', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gtfs.calendar')),
                ('shape', models.ForeignKey(blank=True, help_text='Forma de la ruta.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='gtfs.shape')),
            ],
            options={
                'verbose_name': 'trip',
                'verbose_name_plural': 'trips',
            },
        ),
        migrations.CreateModel(
            name='StopTime',
            fields=[
                ('id', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('arrival_time', models.TimeField(blank=True, default=None, help_text='Hora de llegada. Debe configurarse para las últimas paradas del viaje.', null=True)),
                ('departure_time', models.TimeField(blank=True, default=None, help_text='Hora de salida. Debe configurarse para las últimas paradas del viaje.', null=True)),
                ('stop_sequence', models.PositiveIntegerField()),
                ('stop_headsign', models.CharField(blank=True, help_text='Texto de referencia que identifica la parada para los pasajeros.', max_length=255)),
                ('pickup_type', models.CharField(blank=True, choices=[('0', 'Recogida programada regularmente.'), ('1', 'No hay recogida disponible.'), ('2', 'Debe llamar a la agencia para coordinar recogida.'), ('3', 'Debe coordinar con conductor para agendar recogida.')], help_text='¿Cómo se recoge a los pasajeros?', max_length=1)),
                ('drop_off_type', models.CharField(blank=True, choices=[('0', 'Llegadas programadas regularmente.'), ('1', 'No hay llegadas disponibles.'), ('2', 'Debe llamar a la agencia para coordinar llegada.'), ('3', 'Debe coordinar con el conductor para agendar la llegada.')], help_text='¿Cómo se deja a los pasajeros en su destino?', max_length=1)),
                ('shape_dist_traveled', models.FloatField(blank=True, default=0.0, help_text='Distance of stop from start of shape', null=True)),
                ('timepoint', models.CharField(blank=True, choices=[('0', 'Hora aproximada'), ('1', 'Hora exacta')], default=0, help_text='Exactitud de la hora de llegada y salida.', max_length=1)),
                ('feed_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gtfs.feed')),
                ('stop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gtfs.stop')),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gtfs.trip')),
            ],
            options={
                'verbose_name': 'stop time',
                'verbose_name_plural': 'stop times',
            },
        ),
        migrations.AddField(
            model_name='stop',
            name='zone',
            field=models.ForeignKey(blank=True, help_text='Zona tarifaria para esta parada.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='gtfs.zone'),
        ),
        migrations.CreateModel(
            name='GeoShape',
            fields=[
                ('id', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('shape_id', models.CharField(db_index=True, help_text='Identificador único de una trayectoria.', max_length=255)),
                ('geometry', django.contrib.gis.db.models.fields.LineStringField(help_text='Geometría de la trayectoria.', srid=4326)),
                ('feed_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gtfs.feed')),
            ],
        ),
        migrations.CreateModel(
            name='FeedInfo',
            fields=[
                ('id', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('publisher_name', models.CharField(help_text='Quiénes hicieron el GTFS.', max_length=128)),
                ('publisher_url', models.URLField(blank=True, help_text='URL de los que hicieron el GTFS.')),
                ('lang', models.CharField(blank=True, help_text='Código ISO 639-1 de idioma del suministro.', max_length=2)),
                ('start_date', models.DateField(blank=True, help_text='Fecha en inicia la validez del suministro GTFS.', null=True)),
                ('end_date', models.DateField(blank=True, help_text='Fecha en termina la validez del suministro GTFS.', null=True)),
                ('version', models.CharField(max_length=32)),
                ('contact_email', models.EmailField(blank=True, help_text='Correo electrónico de contacto sobre GTFS.', max_length=128)),
                ('feed_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gtfs.feed')),
            ],
            options={
                'verbose_name': 'feed info',
                'verbose_name_plural': 'feed info objects',
            },
        ),
        migrations.CreateModel(
            name='FareRule',
            fields=[
                ('id', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destination_id', to='gtfs.zone')),
                ('fare', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gtfs.fareattribute')),
                ('feed_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gtfs.feed')),
                ('origin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='origin_id', to='gtfs.zone')),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gtfs.route')),
            ],
            options={
                'verbose_name': 'fare rule',
                'verbose_name_plural': 'fare rules',
            },
        ),
        migrations.AddField(
            model_name='fareattribute',
            name='feed_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gtfs.feed'),
        ),
        migrations.CreateModel(
            name='CalendarDate',
            fields=[
                ('id', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('date', models.DateField(default=None, help_text='Fecha en que se aplica el feriado.')),
                ('exception_type', models.CharField(choices=[('1', 'El servicio ha sido agregado para la fecha especificada.'), ('2', 'El servicio ha sido removido de la fecha especificada.')], help_text='¿Agregar o remover servicio?', max_length=1)),
                ('holiday_name', models.CharField(help_text='Nombre oficial del feriado.', max_length=64)),
                ('feed_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gtfs.feed')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gtfs.calendar')),
            ],
            options={
                'verbose_name': 'calendar date',
                'verbose_name_plural': 'calendar dates',
            },
        ),
        migrations.AddField(
            model_name='calendar',
            name='feed_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gtfs.feed'),
        ),
        migrations.AddField(
            model_name='agency',
            name='feed_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gtfs.feed'),
        ),
    ]
