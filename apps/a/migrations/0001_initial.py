# Generated by Django 2.2 on 2019-08-01 01:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0001_initial'),
        ('vehicle', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('In', 'In'), ('Out', 'Out')], default='re', max_length=4)),
                ('total', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receipt_number', models.CharField(max_length=12)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('payment', models.CharField(choices=[('cs', 'cash'), ('ca', 'card'), ('cu', 'cupon')], max_length=2)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='client.Client')),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='receipt.Order')),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('Vehicle', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='vehicle.Vehicle')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='receipt.Order')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='vehicle',
            field=models.ManyToManyField(through='receipt.OrderDetail', to='vehicle.Vehicle'),
        ),
    ]
