class CreateTickets < ActiveRecord::Migration
  def change
    create_table :tickets do |t|
      t.references :project
      t.references :status
      t.string :name, :limit => 30
      t.text :description
      t.datetime :start_date
      t.datetime :end_date
      t.integer :owner_id
      t.timestamps
    end
  end
end
