class CreateProjects < ActiveRecord::Migration
  def change
    create_table :projects do |t|
      t.string :name, :limit => 20
      t.text :description
      t.datetime :start_date
      t.datetime :end_date
      t.integer :owner_id
      t.timestamps
    end
  end
end
