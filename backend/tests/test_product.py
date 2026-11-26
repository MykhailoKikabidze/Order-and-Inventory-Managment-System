from catalogue.models import Product
from django.db import IntegrityError, transaction
from django.test import TestCase


class ProductTest(TestCase):
    def test_sku_is_unique_ignoring_case(self):
        test_product = Product(
            sku='ABC-1',
            name='Test Product',
            description='Test Description',
            base_unit='kg',
            is_active=True
        )
        test_product.save()

        with self.assertRaises(IntegrityError), transaction.atomic():
            duplicate_product = Product(
                sku='abc-1',
                name='Test Product 2',
                description='Test Description 2',
                base_unit='kg',
                is_active=True
            )
            duplicate_product.save()

    def test_sku_is_unique_ignoring_case_for_inactive_product(self):
        test_product = Product(
            sku='ABC-1',
            name='Test Product',
            description='Test Description',
            base_unit='kg',
            is_active=False
        )
        test_product.save()

        with self.assertRaises(IntegrityError), transaction.atomic():
            duplicate_product = Product(
                sku='abc-1',
                name='Test Product 2',
                description='Test Description 2',
                base_unit='kg',
                is_active=True
            )
            duplicate_product.save()

    def test_invalid_base_unit_is_rejected(self):
        with self.assertRaises(IntegrityError), transaction.atomic():
            test_product = Product(
                sku='ABC-1',
                name='Test Product',
                description='Test Description',
                base_unit='box',
                is_active=True
            )
            test_product.save()

    def test_product_sku_whitespace_validation(self):
        with self.assertRaises(IntegrityError), transaction.atomic():
            test_product = Product(
                sku='\t\n',
                name='Test Product',
                description='Test Description',
                base_unit='kg',
                is_active=True
            )
            test_product.save()

    def test_product_name_whitespace_validation(self):
        with self.assertRaises(IntegrityError), transaction.atomic():
            test_product = Product(
                sku='ABC-1',
                name='\t\n',
                description='Test Description',
                base_unit='kg',
                is_active=True
            )
            test_product.save()

    def test_product_sku_empty_string_validation(self):
        with self.assertRaises(IntegrityError), transaction.atomic():
            test_product = Product(
                sku='',
                name='Test Product',
                description='Test Description',
                base_unit='kg',
                is_active=True
            )
            test_product.save()

    def test_product_name_empty_string_validation(self):
        with self.assertRaises(IntegrityError), transaction.atomic():
            test_product = Product(
                sku='ABC-1',
                name='',
                description='Test Description',
                base_unit='kg',
                is_active=True
            )
            test_product.save()

    